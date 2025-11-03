"""
Please run this program with your default browser open.
"""
import requests
import argparse
from collections import defaultdict
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Function to fetch aggregated data from OONI API
def fetch_aggregation_data(probe_cc, domain, since, until):
    url = f"https://api.ooni.org/api/v1/aggregation?probe_cc={probe_cc}&since={since}&until={until}&time_grain=day&axis_x=measurement_start_day&test_name=web_connectivity&domain={domain}"
    response = requests.get(url)
    return response.json()  # Returns a dictionary with daily aggregation data

# Function to fetch detailed measurement data from OONI API for each day
def fetch_measurements_data(probe_cc, domain, date):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    
    # Subtract one day from the given date
    previous_day = date_obj - timedelta(days=1)
    
    # Format the new 'since' date as a string
    since_date = previous_day.strftime("%Y-%m-%d")
    
    # Use the same 'until' date (which is the current date)
    until_date = date
    
    # Construct the API URL
    url = f"https://api.ooni.org/api/v1/measurements?probe_cc={probe_cc}&domain={domain}&test_name=web_connectivity&since={since_date}&until={until_date}&limit=50&order=desc"
    response = requests.get(url)
    return response.json()  # Returns a list of measurements for that date

# Function to process detailed measurement data and classify failures
def classify_failures_from_measurements(measurements_data):
    failures = defaultdict(int)
    
    # Iterate over the measurements and classify each based on blocking type
    for measurement in measurements_data.get('results', []):  # Ensure we have results to iterate
        analysis = measurement.get('scores', {}).get('analysis', {}).get('blocking_type', None)
        
        if analysis:
            if 'http-failure' in analysis:
                failures['HTTP failure'] += 1
            elif 'dns' in analysis:
                failures['DNS failure'] += 1
            else:
                failures['Other failure'] += 1
    
    return failures

# Function to summarize the aggregated data and classify the total success/failure
def summarize_data(aggregation_data, probe_cc, domain):
    total_success = 0
    total_failure = defaultdict(int)
    
    # Iterate over the aggregation data (which is a dictionary of daily results)
    for day_data in aggregation_data.get('result', []):  # Access the 'result' key
        date = day_data['measurement_start_day']
        
        # Fetch the detailed measurements for the day
        measurements_data = fetch_measurements_data(probe_cc, domain, date)
        
        # Classify failures for the given day's measurements
        failures = classify_failures_from_measurements(measurements_data)
        
        total_success += day_data.get('ok_count', 0)
        for failure_type, count in failures.items():
            total_failure[failure_type] += count
    
    return total_success, total_failure

# Function to generate the stacked bar chart using Plotly
def generate_bar_chart(total_success, total_failure,args):
    # Prepare the categories and values for the stacked bar
    categories = ['Success', 'HTTP failure', 'DNS failure', 'Other failure']
    values = [
        total_success,
        total_failure.get('HTTP failure', 0),
        total_failure.get('DNS failure', 0),
        total_failure.get('Other failure', 0)
    ]
    
    # Create the plot
    fig = go.Figure(data=[
        go.Bar(
            y=categories,
            x=values,
            orientation='h',
            name='Results',
            marker=dict(color=['green', 'red', 'orange', 'purple'])  # Color for each section
        )
    ])

    # Customize layout to make it more clear and visually appealing
    fig.update_layout(
        title='VPN Website blocking method breakdown, country: '+args.country_code+', date range '+args.since+' to '+args.until,
        xaxis_title='Count',
        yaxis_title='Outcome',
        barmode='stack',
        template='plotly_dark',
    )

    # Show the interactive plot
    fig.show()

# Main function to tie everything together
def main():
    # Argument parser for command-line inputs
    parser = argparse.ArgumentParser(description='Fetch and visualize OONI test results.')
    parser.add_argument('--country_code', default='RU', help='Country code (default: RU)')
    parser.add_argument('--since', default='2025-10-25', help='Start date (default: 2025-10-01)')
    parser.add_argument('--until', default='2025-11-01', help='End date (default: 2025-11-01)')
    args = parser.parse_args()

    # Fetch data for both domains (surfshark.com and nordvpn.com)
    domains = ['surfshark.com', 'nordvpn.com']
    total_success = 0
    total_failure = defaultdict(int)

    for domain in domains:
        print(f"Fetching data for {domain}...")
        
        # Fetch aggregation data (returns a dictionary where values are the daily aggregation data)
        aggregation_data = fetch_aggregation_data(args.country_code, domain, args.since, args.until)
        
        # Summarize the results (fetch detailed measurements and classify failures)
        success, failure = summarize_data(aggregation_data, args.country_code, domain)
        total_success += success
        for failure_type, count in failure.items():
            total_failure[failure_type] += count

    # Generate and display the bar chart
    generate_bar_chart(total_success, total_failure, args)

if __name__ == '__main__':
    main()
