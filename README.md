# Open Measurement Hackathon

# @ ACM IMC 2025

[**Agenda	2**](#agenda)

[**Datasets and Projects	2**](#datasets-and-projects)

[Cloudflare Radar	2](#cloudflare-radar)

[Description	2](#description)

[Creating a Cloudflare account	3](#creating-a-cloudflare-account)

[Creating an API token	3](#creating-an-api-token)

[OONI	4](#ooni)

[Description	4](#description-1)

[Project ideas	5](#project-ideas)

[\[OONI \- Project 1\] Analyze and visualize internet censorship data	5](#[ooni---project-1]-analyze-and-visualize-internet-censorship-data)

[\[OONI \- Project 2\] Encrypted Client Hello (ECH) blocking	5](#[ooni---project-2]-encrypted-client-hello-\(ech\)-blocking)

[\[OONI \- Project 3\] Automatic detection of blocking signals	5](#[ooni---project-3]-automatic-detection-of-blocking-signals)

[\[OONI \- Project 4\] Examine TLS certificate diversity across countries/networks	6](#[ooni---project-4]-examine-tls-certificate-diversity-across-countries/networks)

[\[OONI \- Project 5\] Investigate misbehaving OONI Probes	6](#[ooni---project-5]-investigate-misbehaving-ooni-probes)

[M-Lab	6](#m-lab)

[Description	6](#description-2)

[Project ideas	7](#project-ideas-1)

[\[M-Lab \- Project 1\] Load balancing M-Lab: Smarter M-Lab server deployment	7](#[m-lab---project-1]-load-balancing-m-lab:-smarter-m-lab-server-deployment)

[\[M-Lab \- Project 2\]  Mapping M-Lab platform’s global connectivity	7](#[m-lab---project-2]-mapping-m-lab-platform’s-global-connectivity)

[\[M-Lab \- Project 3\]  Detecting Internet shutdowns from user reactions	8](#[m-lab---project-3]-detecting-internet-shutdowns-from-user-reactions)

[\[M-Lab \- Project 4\]  “CensorScope”: Dashboards for Internet shutdown and throttling detection	9](#[m-lab---project-4]-“censorscope”:-dashboards-for-internet-shutdown-and-throttling-detection)

[\[M-Lab \- Project 5\]  Internet Quality Barometer (IQB) in action	10](#[m-lab---project-5]-internet-quality-barometer-\(iqb\)-in-action)

[\[M-Lab \- Project 6\]  “State of the Net”: Interactive Internet performance reports	10](#[m-lab---project-6]-“state-of-the-net”:-interactive-internet-performance-reports)

[\[M-Lab \- Project 7\]  “TCP Showdown”: Comparing MSAK and NDT Measurements	11](#[m-lab---project-7]-“tcp-showdown”:-comparing-msak-and-ndt-measurements)

[\[M-Lab \- Project 8\]  Internet Topology Visualization: Mapping Network Paths from Traceroute Data	11](#[m-lab---project-8]-internet-topology-visualization:-mapping-network-paths-from-traceroute-data)

[IIJ \- Internet Yellow Pages	12](#iij---internet-yellow-pages)

[Description	12](#description-3)

[Project ideas	13](#project-ideas-2)

[\[IIJ \- Project 1\] Visualization of IYP data	13](#[iij---project-1]-visualization-of-iyp-data)

[\[IIJ \- Project 2\] Your research with IYP	13](#[iij---project-2]-your-research-with-iyp)

[\[IIJ \- Project 3\] Adding data to IYP	13](#[iij---project-3]-adding-data-to-iyp)

[\[IIJ \- Project 3\] Web centralization	13](#[iij---project-3]-web-centralization)

[Reverse Traceroute	14](#reverse-traceroute)

[Description	14](#description-4)

[Project Ideas	14](#project-ideas-3)

[\[RevTr \- Project 1\] General Study	14](#[revtr---project-1]-general-study)

[\[RevTr \- Project 2\] WeHeY Integration with RevTr	14](#[revtr---project-2]-wehey-integration-with-revtr)

[\[RevTr \- Project 3\] Poiroot Coverage with RevTr	15](#[revtr---project-3]-poiroot-coverage-with-revtr)

# 

# **Agenda** {#agenda}

**Agenda**  
13:00-14:00	Introduction to datasets and team formation  
14:00-19:00	Time for analysis\!  
19:00-20:00	Share outs

**Location**  
Discovery Building, 330 N. Orchard St, Madison, WI 53715

**Webpage (@IMC website)**   
[https://conferences.sigcomm.org/imc/2025/events/hackathon/](https://conferences.sigcomm.org/imc/2025/events/hackathon/) 

# 

# **Datasets and Projects** {#datasets-and-projects}

## **Cloudflare Radar** {#cloudflare-radar}

### **Description** {#description}

Cloudflare Radar is a hub that showcases global Internet traffic, attack, and technology trends and insights. Cloudflare Radar is powered by data from Cloudflare's global network, as well as aggregated and anonymized data from Cloudflare's 1.1.1.1 public DNS Resolver. 

In some cases Cloudflare Radar uses data from [PeeringDB](https://www.peeringdb.com/) (interconnection meta-information) and [APNIC](https://stats.labs.apnic.net/aspop/) (visible ASNs customer population measurements).

With Radar, you can access trends and insights, like the adoption of new technologies, browsers or operating systems. Radar also keeps up to date with relevant events around the world to provide information on Internet activity patterns.

[https://radar.cloudflare.com/](https://radar.cloudflare.com/) is built on top of the Radar API ([specification](https://developers.cloudflare.com/api/resources/radar/), [documentation](https://developers.cloudflare.com/radar/)).

The Radar Data Explorer ([https://radar.cloudflare.com/explorer](https://radar.cloudflare.com/explorer)) is a web-based interface designed to simplify the process of building, and viewing the results of, more complex API queries. It also provides example API calls and responses for the queries built using the interface. More information is available at [https://blog.cloudflare.com/radar-data-explorer-ai-assistant/\#building-a-query-directly](https://blog.cloudflare.com/radar-data-explorer-ai-assistant/#building-a-query-directly)

A free Cloudflare account is required to generate an API token that is needed to make API queries. If you do not currently have a Cloudflare account, or have not yet generated the necessary token, please follow these steps…

#### Creating a Cloudflare account {#creating-a-cloudflare-account}

* Go to [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)  
* If you want to login with your Google, Apple, or Github accounts, click the appropriate link.  
* Otherwise, enter your email address and a password in the appropriate fields, check the box to verify that you are a human, and click “Sign up”.  
* Click the link in the “\[Action required\] Verify your email address” email sent to the address associated with the account.

#### Creating an API token {#creating-an-api-token}

* Login to the Cloudflare dash at [https://dash.cloudflare.com/login](https://dash.cloudflare.com/login)  
* Click the profile icon in the upper right corner, and click “Profile” in the drop-down menu.  
* On the Profile page, click “API Tokens” from the left-side navigation bar.  
* Click the “Create Token” button in the “API Tokens” card on the “User API Tokens” page.  
* Click the “Use template” button next to “Read Cloudflare Radar data”  
* Under “Account Resources”, choose the account associated with your login from the drop-down menu.  
* Click the “Continue to summary” button at the bottom of the page.  
* Click “Create Token” on the next page  
* If token creation was successful, it will be displayed in a text box. Copy it to a password manager or other secure location, as it will not be shown again. You can confirm that the token is valid and active by executing the curl command shown on the page.

## 

## **OONI** {#ooni}

### **Description** {#description-1}

Since 2012, OONI has openly published [more than 2 billion network measurements](https://explorer.ooni.org/) collected from 29 thousand ASes in 242 countries and territories. These measurements have been collected and contributed by [OONI Probe](https://ooni.org/install/) users around the world. Every minute, new measurements are published in near real-time.

OONI data can be accessed through the public [OONI Explorer web interface](https://explorer.ooni.org/). OONI Explorer has a component called the [Measurement Aggregation Toolkit](https://explorer.ooni.org/chart/mat) (MAT), which can be used to produce plots of measurements over time. OONI Explorer is backed by [OONI API](https://api.ooni.org/apidocs/), links for the relevant API endpoints used to produce the charts can be found by clicking on the JSON Data or CSV Data on the MAT pages.

It’s worth noting that the OONI API is not suitable for retrieving large volumes of data and it's recommended instead to query the clickhouse database directly. For some more advanced use cases it’s also possible to [download the raw measurements directly from s3](https://docs.ooni.org/data/).

For the IMC hackathon we are also offering direct access to the underlying clickhouse database, the schema of which is available in the relevant documentation page: [https://docs.ooni.org/data/oonidata-analysis-db/](https://docs.ooni.org/data/oonidata-analysis-db/).

In order to query the clickhouse database you may use the following credentials to access the OONI jupyter notebook server:

URL: https://notebook.ooni.org/

user: imc2025  
password: aGoodUserIsAGentleUser

Please note that this is a shared instance, so please try to limit resource usage as much as possible. If you need to run particularly memory or CPU heavy computation it’s recommended you export a dump of the data and run these computations on your own machine.

Other relevant documentation on accessing and analysing OONI data can be found at the following links:

* OONI Explorer MAT: [https://ooni.org/support/ooni-explorer/\#measurement-aggregation-toolkit-mat](https://ooni.org/support/ooni-explorer/#measurement-aggregation-toolkit-mat)  
* Interpreting OONI Data: [https://ooni.org/support/interpreting-ooni-data/](https://ooni.org/support/interpreting-ooni-data/)  
* OONI base data format specifications: [https://github.com/ooni/spec/tree/master/data-formats](https://github.com/ooni/spec/tree/master/data-formats)  
* OONI Test specifications: [https://github.com/ooni/spec/tree/master/nettests](https://github.com/ooni/spec/tree/master/nettests)  
* OONI Database schema: [https://docs.ooni.org/data/oonidata-analysis-db/](https://docs.ooni.org/data/oonidata-analysis-db/)   
* Fetching OONI data from Amazon S3: [https://docs.ooni.org/data/](https://docs.ooni.org/data/) 

If you run into any issues, since the OONI team will not be in person at IMC, you should reach out to the OONI team and community on the public slack channel \#ooni-dev on [https://slack.ooni.org/](https://slack.ooni.org/) (you can sign up for an account by entering your email address and then join the \#ooni-dev channel).

### **Project ideas** {#project-ideas}

#### \[OONI \- Project 1\] Analyze and visualize internet censorship data {#[ooni---project-1]-analyze-and-visualize-internet-censorship-data}

OONI created the [Measurement Aggregation Toolkit (MAT)](https://explorer.ooni.org/chart/mat) which enables you to track internet censorship around the world and create your own custom charts based on real-time OONI network measurement data. As part of this challenge, we invite you to analyze OONI data and create your own data visualization(s) based on the questions you would like to answer.

For example, this could involve exploring the following questions based on OONI data:

* Which circumvention technologies (among the [ones measured by OONI](https://ooni.org/nettest#tor)) are most effective nowadays at a given location? Is there a trend (increase or decrease) in such effectiveness?  
* Where in the world are located the sites that appear blocked from a given location?  
* Which censorship techniques are adopted in X country? A novel visualization could depict blocking techniques in use, sorted by degree of sophistication. Live filtering according to blocking techniques could also be useful in terms of visualization overlays.

#### \[OONI \- Project 2\] Encrypted Client Hello (ECH) blocking {#[ooni---project-2]-encrypted-client-hello-(ech)-blocking}

OONI has a test for measuring Encrypted Client Hello (ECH) called echcheck ([https://github.com/ooni/spec/blob/master/nettests/ts-039-echcheck.md](https://github.com/ooni/spec/blob/master/nettests/ts-039-echcheck.md)). There are reports of ECH being blocked in Russia when used in conjunction with the cloudflare outer\_sni [cloudflare-ech.com](http://cloudflare-ech.com) (see: [https://github.com/net4people/bbs/issues/417](https://github.com/net4people/bbs/issues/417)).

It would be interesting to study the evolution of this block in Russia, but also investigate if we see a signal of it getting blocked in other regions as well.  

**Tips**

* Relevant DB columns in obs\_web table are: tls\_echconfig, tls\_outer\_server\_name, tls\_server\_name, tls\_failure

#### \[OONI \- Project 3\] Automatic detection of blocking signals {#[ooni---project-3]-automatic-detection-of-blocking-signals}

This project is about applying automated methods to identify changes in blocking in a particular country, ASN pair. It may involve looking at absolute volume of measurements, as we anecdotally have seen users start running OONI Probe more frequently when something starts to be blocked in a certain country, or making use of some of the features in the fastpath or analysis\_web\_measurements tables.

**Tips**

* Experiment with different changepoint detection algorithms to identify shifts in blocking patterns within a hostname, probe\_cc, probe\_asn tuple (eg. CUSUM, BOCPD, etc.)  
* For the analysis table use the (dns|tcp|tls)\_(blocked|ok) metrics grouped by probe\_cc, probe\_asn, resolver\_asn on the analysis\_web\_measurements table 

#### \[OONI \- Project 4\] Examine TLS certificate diversity across countries/networks {#[ooni---project-4]-examine-tls-certificate-diversity-across-countries/networks}

This is about examining when a specific domain name presents a TLS certificate that is different or issued by a different authority depending on the vantage point that carried out the measurements.  
While this can be a signal of censorship, in the event of an attempted TLS MiTM, it may also happen as a result of a different TLS certificate being used depending on the location of the server hosting the site.

**Tips**

* Look in the obs\_web table for the tls\_end\_entity\_\* columns

#### \[OONI \- Project 5\] Investigate misbehaving OONI Probes {#[ooni---project-5]-investigate-misbehaving-ooni-probes}

OONI has multiple probe apps, with different versions, running our test engine with different versions.

Can you tell if any of our apps/engines is misbehaving, compared with the rest?   
For example, providing constantly different results for the same tests and networks? 

**Tips**

* Fields to look for: software\_name, software\_version, engine\_name, engine\_version and the outcomes from the fastpath (eg. msm\_failure, anomaly, confirmed) or obs\_web tables

## 

## **M-Lab** {#m-lab}

### **Description** {#description-2}

* Intro Video [https://youtu.be/r767hjoTo4E](https://youtu.be/r767hjoTo4E)	  
* Get access to data   
  * To access M-Lab’s public data, you need to sign up for the discuss@ list [https://groups.google.com/a/measurementlab.net/g/discuss?pli=1](https://groups.google.com/a/measurementlab.net/g/discuss?pli=1)   
  * Then you can access the data through BigQuery  
    * Tutorial: [https://www.measurementlab.net/data/docs/bq/quickstart/](https://www.measurementlab.net/data/docs/bq/quickstart/)   
    * Data at BigQuery: [https://console.cloud.google.com/bigquery?project=measurement-lab](https://console.cloud.google.com/bigquery?project=measurement-lab)    
    * Schema (for ndt7 dataset): [https://www.measurementlab.net/tests/ndt/ndt7/](https://www.measurementlab.net/tests/ndt/ndt7/)   
* Example Queries / Collabs:  
  * [IMC 2023](https://colab.research.google.com/drive/1DKzJH3RSbVqkeedVFlmPQbTyACYO9aAC)   
  * [Optima shutdown example](https://colab.research.google.com/drive/1z9YMpvLs9JzkQPBbvdGFGt6Vzy8-EYxg#scrollTo=I1yXIEbLn7ne%20) 

### **Project ideas** {#project-ideas-1}

#### \[M-Lab \- Project 1\] Load balancing M-Lab: Smarter M-Lab server deployment {#[m-lab---project-1]-load-balancing-m-lab:-smarter-m-lab-server-deployment}

**Goal**: Model the traffic load of M-Lab platform and optimize for server deployments

**What:** When a user runs a speedtest in the M-Lab platform, the “Locate” service of M-Lab selects which of the 500+ servers will serve the test of the user. Locate typically selects servers based on geographical proximity to users. There are a number of research questions that could help to improve the M-Lab platform: *What is the traffic load (i.e., number of tests) per M-Lab server? How would this change if we add new servers and/or remove existing servers from the platform? How can we select deployment locations for new servers?*  
The goal is to develop a tool (code, or colab, or web app, etc) that based on past statistics of tests to calculate the traffic per server. The traffic depends on server location, server configuration, and users’ location. The globe can be split as a Voronoi map, based on servers; adding/removing servers changes this Voronoi map. Having this tool can enable the next step of analysis for optimizing new server deployments to satisfy objectives, such as offloading an existing server or decreasing the user-server distance (e.g., taking into account the population per region) or increasing the geographical coverage of M-Lab. 

**Datasets**: 

* M-Lab BigQuery  
* \[optional\] Internet Yellow Pages, other

**Contact person**:

* M-Lab: Pavlos Sermpezis (pavlos@measurementlab.net)


#### \[M-Lab \- Project 2\]  Mapping M-Lab platform’s global connectivity {#[m-lab---project-2]-mapping-m-lab-platform’s-global-connectivity}

**Goal**: Map/characterize how M-Lab servers are connected to the Internet

**What:** Analyze and characterize the connectivity of M-Lab servers to the Internet. Analysis may include distances (in AS-hops or IP-hops) to top client ASNs or top ISPs per region, connectivity to IXPs, etc. The analysis can be done using M-Lab measurements (traceroutes) and/or other Internet routing datasets (traceroutes, BGP data, Internet Yellow Pages database, etc.). Generate a report per server and/or visualizations, detect if any main connectivity limitations, and recommend improvements

**Datasets**: 

* M-Lab BigQuery  
* Other datasets: Internet routing data Connectivity (RIPE Atlas, BGP data, IODA, IIJ, etc.)

**Contact person**:

* M-Lab: Pavlos Sermpezis (pavlos@measurementlab.net)

#### \[M-Lab \- Project 3\]  Detecting Internet shutdowns from user reactions {#[m-lab---project-3]-detecting-internet-shutdowns-from-user-reactions}

**Goal**: Analyze user behavior upon Internet shutdowns. Design methodology to automatically detect Internet shutdowns based on the analysis.

**What:** Users take speedtests (e.g., using M-Lab platform) to check their Internet connectivity and performance. Upon Internet outages or other events, typically users tend to do more tests to troubleshoot their connectivity. This behavior of users (which can be observed in the data) can be a powerful signal for detecting Internet outages (which cannot be directly observed in the data). The goal of this project is to provide answers to the following research questions: *How do users react upon Internet shutdowns, censorship or interruption events? Can we design a methodology for automated detection of these events based on user patterns?*  
This can be done by analyzing M-Lab data, i.e., number of user tests before, after, and during Internet events to identify patterns. E.g., do users start running more tests than usual just after an event? For how long? Do we see large peaks or steady increase in tests? When do users stop running tests? And how does this differ among event types, event durations, geographical regions, or other factors?   
Based on the initial analysis, can we design a methodology (e.g., threshold/rule-based, ML/AI, or other) to automatically detect events?

**Datasets**: 

* M-Lab BigQuery  
* List on Internet events  
  * Radar outage center [https://radar.cloudflare.com/outage-center\#internet-outages](https://radar.cloudflare.com/outage-center#internet-outages). Also available through the Radar API: [https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/](https://developers.cloudflare.com/api/resources/radar/subresources/annotations/subresources/outages/)  
  * OONI Explorer findings page: [https://explorer.ooni.org/findings](https://explorer.ooni.org/findings). Also available through the API [https://oonifindings.prod.ooni.io/docs](https://oonifindings.prod.ooni.io/docs)  
* \[optional\] Mozilla Network Outages Data Project [https://wiki.mozilla.org/Mozilla\_Network\_Outages\_Data\_Project](https://wiki.mozilla.org/Mozilla_Network_Outages_Data_Project) 

**Contact person**:

* M-Lab: Pavlos Sermpezis ([pavlos@measurementlab.net](mailto:pavlos@measurementlab.net))  
* OONI: Arturo Filastò (arturo@ooni.org)

### 

#### \[M-Lab \- Project 4\]  “CensorScope”: Dashboards for Internet shutdown and throttling detection {#[m-lab---project-4]-“censorscope”:-dashboards-for-internet-shutdown-and-throttling-detection}

**Goal**: Use M-Lab data to derive insights for supporting detection/characterisation of Internet censorship or shutdown events

**What:** When an Internet outage, censorship or shutdown event takes place, it affects the Internet performance that users experience. This Internet performance is reflected in M-Lab data. How can M-Lab data be used to derive insights that support identification/characterisation of Internet censorship or shutdown events?  
The goal is to create a dashboard and/or a colab and/or a set of visualizations to analyze M-Lab data for cases related to Internet censorship or shutdown events.   
The information that can be used to infer and explore events related to Internet connectivity is:

* Number of tests within a time interval (e.g., hourly, daily, or other custom range)  
* Statistics about download/upload throughput (e.g., mean, median, 95th percentile)

filtered and/or aggregated by client’s and/or server’s *network* (ASN, prefix) and/or *geography (*country, region, city, lat/lon, etc.)

Example ideas:

* An increase in the number of tests in an region may indicate connectivity degradation (i.e., users observe poor performance and navigate to the speed test to check their access)  
* An decrease in the number of tests in a region (e.g., in particular if for a given network this numbers decreases to zero) may indicate loss of connectivity  
* A change in the statistics of download throughput can be related to significant changes in the network configuration and or censorship processes (e.g. throttling).  
* Changes in (reverse) traceroute hops between clients in a region.

A related project with some examples for a similar use case: Ukraine Pulse project comparing before and after war performance metrics used M-Lab data [https://lookerstudio.google.com/reporting/90c38a5d-c9f8-47dc-94a4-ef913afa2eac](https://lookerstudio.google.com/reporting/90c38a5d-c9f8-47dc-94a4-ef913afa2eac) 

**Datasets**: 

* M-Lab BigQuery  
* OONI Explorer findings page: [https://explorer.ooni.org/findings](https://explorer.ooni.org/findings). Also available through the API [https://oonifindings.prod.ooni.io/docs](https://oonifindings.prod.ooni.io/docs)  
* Other

**Contact person**:

* M-Lab: Pavlos Sermpezis ([pavlos@measurementlab.net](mailto:pavlos@measurementlab.net))  
* OONI: Arturo Filastò (arturo@ooni.org)

#### \[M-Lab \- Project 5\]  Internet Quality Barometer (IQB) in action {#[m-lab---project-5]-internet-quality-barometer-(iqb)-in-action}

**Goal**: Implement an instance of the IQB framework for a region using multiple datasets

**What:** IQB is a comprehensive framework for collecting data and calculating a composite score, the “IQB Score”, which reflects the quality of Internet experience. IQB takes a more holistic approach than “speed tests” and evaluates Internet performance across various use cases (web browsing, video streaming, online gaming, etc.), each with its own specific network requirements (latency, throughput, etc.). Learn more about IQB at [https://www.measurementlab.net/blog/iqb/](https://www.measurementlab.net/blog/iqb/)   
The goal of this project will be to develop code (e.g., colab) to implement the IQB framework for a region (e.g., country) using multiple datasets. The implementation will need to collect data from M-Lab, Oookla, Cloudflare, etc. to calculate metrics for the region and plug the data in the IQB formula

**Datasets**: 

* M-Lab  
* Ookla  
* Cloudflare

**Contact person**:

* M-Lab: Pavlos Sermpezis ([pavlos@measurementlab.net](mailto:pavlos@measurementlab.net))

### 

#### \[M-Lab \- Project 6\]  “State of the Net”: Interactive Internet performance reports {#[m-lab---project-6]-“state-of-the-net”:-interactive-internet-performance-reports}

**Goal**: Characterize the Internet performance of a region or network using open measurement datasets.  
**What:** Create a dashboard to analyze open dataset to characterize the Internet performance within a region and/or network. The visualizations can present a set of simple or composite metrics of Internet performance from several datasets, including M-Lab, Cloudflare, IODA, Internet Yellow Pagers, etc.   
*\[Optional\]* Use an AI agent (e.g., LLM-based) to explain the dashboard results and interact with the user.

**Datasets**: 

* M-Lab  
* Cloudflare

**Contact person**:

* M-Lab: Pavlos Sermpezis ([pavlos@measurementlab.net](mailto:pavlos@measurementlab.net))

#### \[M-Lab \- Project 7\]  “TCP Showdown”: Comparing MSAK and NDT Measurements {#[m-lab---project-7]-“tcp-showdown”:-comparing-msak-and-ndt-measurements}

**Goal**: How do M-Lab measurements differ based on the TCP congestion control algorithm and number of streams used? 

**What:** Analyze M-Lab data, and compare measurement between MSAK and NDT to identify if there are major differences, and if yes, what are their characteristics and when/where (e.g., types of networks, geographical locations, etc.) they happen? The goal is to identify parameters that M-Lab can use in their (default) speedtest, as well as to provide recommendations to M-Lab users for selecting their parameters.

**Datasets**: 

* M-Lab BigQuery

**Contact person**:

* M-Lab: Pavlos Sermpezis ([pavlos@measurementlab.net](mailto:pavlos@measurementlab.net)), Roberto D’Auria ([roberto@measurementlab.net](mailto:roberto@measurementlab.net))

#### \[M-Lab \- Project 8\]  Internet Topology Visualization: Mapping Network Paths from Traceroute Data {#[m-lab---project-8]-internet-topology-visualization:-mapping-network-paths-from-traceroute-data}

**Goal:** How can we effectively visualize and understand the physical and logical structure of internet routing at scale? This project aims to transform raw traceroute measurements into interactive graphical and geographic visualizations that reveal network topology, routing patterns, and infrastructure dependencies across the internet.

**What:**  
Analyze large-scale traceroute data from M-Lab's IPRS dataset to:

* Extract and process network topology from multipath traceroute measurements stored in BigQuery  
* Geocode network infrastructure by mapping IP addresses to real-world geographic location approximations  
* Visualize routing patterns using interactive web-based maps that show how internet traffic flows between continents, countries, and cities  
* Identify network characteristics including:  
* Major internet exchange points (IXPs) and hub locations  
* Route redundancy and multipath routing behavior  
* ISP backbone infrastructure and peering relationships

**Datasets**:

* M-Lab IPRS (Internet Path Routing Study) BigQuery tables  
* IP Geolocation: IPInfo API for router location mapping

**Contact person**:

* Dioptra: Zeynep Arslan ([zeyneparslan.lip6@gmail.com](mailto:zeyneparslan.lip6@gmail.com)), Timur Friedman ([timur.friedman.work@gmail.com](mailto:timur.friedman.work@gmail.com)) 

## 

## **IIJ \- Internet Yellow Pages** {#iij---internet-yellow-pages}

### **Description** {#description-3}

The Internet Yellow Pages (IYP) is a graph database composed of over 60 Internet measurement datasets. IYP has been designed to facilitate the exploration and analysis of these datasets. An overview can be found in the paper “[The Wisdom of the Measurement Crowd: Building the Internet Yellow Pages a Knowledge Graph for the Internet](https://www.iijlab.net/en/members/romain/pdf/romain_imc2024.pdf).” 

The easiest way to browse the IYP database is to visit the [Internet Health Report website](https://www.ihr.live). There you can search for an Internet resource (e.g. AS, prefix, domain name) and get IYP data related to that resource.

1. Enter the resource into the **search field** in the top left corner.  
2. Selecting the **Routing**, **DNS**, **Peering**, **Registration**, or **Rankings** tabs (the **Monitor** tab is external to the IYP).

For each widget, you’ll find a *chart, data, Cypher query*, and a *metadata* tabs. 

* The Chart tab shows a visual representation of the data.  
* The Data tab gives the raw data in a table format and a link to download the data in CSV format.   
* The Cypher Query tab gives you the exact query we used to pull the data from IYP. You can reuse that to [query directly the IYP database](https://iyp.iijlab.net/iyp/browser/?dbms=iyp-bolt.iijlab.net:443) or craft your own queries. 

IYP is built on Neo4j, a graph database management system, which means that data is stored and queried through graph structures. Neo4j’s query language is called Cypher and all programmatic interaction with IYP will require basic understanding of Cypher.   
To learn how to write your own IYP queries, see the [IYP tutorial](https://docs.google.com/document/d/1cl3oUY-65TluosIjEBgOT3NNXq_UP-ZGQD4waqVvdhs/edit?usp=sharing).  
See also example queries:

* APNIC blog article: [https://blog.apnic.net/2023/09/06/understanding-the-japanese-internet-with-the-internet-yellow-pages/](https://blog.apnic.net/2023/09/06/understanding-the-japanese-internet-with-the-internet-yellow-pages/)  
* IYP Gallery: [https://github.com/InternetHealthReport/internet-yellow-pages/blob/main/documentation/gallery.md](https://github.com/InternetHealthReport/internet-yellow-pages/blob/main/documentation/gallery.md)   
* Jupyter notebooks reproducing two research studies: [https://github.com/InternetHealthReport/iyp-notebooks](https://github.com/InternetHealthReport/iyp-notebooks) 

A public instance of IYP is available at: [https://iyp.iijlab.net](https://iyp.iijlab.net)  
This is sufficient for retrieving small datasets and executing most common queries. For heavier analysis please consider [installing IYP locally](https://docs.google.com/document/d/1cl3oUY-65TluosIjEBgOT3NNXq_UP-ZGQD4waqVvdhs/edit?tab=t.hnwujpcfbxhm).

### **Project ideas** {#project-ideas-2}

#### \[IIJ \- Project 1\] Visualization of IYP data  {#[iij---project-1]-visualization-of-iyp-data}

Create visualizations for IYP data. Fetch data from IYP and plot it with your favorite visualization tools. For example:

* Projection on a map of geolocated infrastructure (PeeringDB, ASRank, Atlas)  
* Selected ASes point of presences using PeeringDB’s co-location facility information  
* Internet population using APNIC AS population and ASRank lat/lon coordinates

#### \[IIJ \- Project 2\] Your research with IYP  {#[iij---project-2]-your-research-with-iyp}

Reproduce your own research with IYP and extend it with the numerous datasets available in IYP. See the [two IYP notebooks](https://github.com/InternetHealthReport/iyp-notebooks) reproducing past studies.

#### \[IIJ \- Project 3\] Adding data to IYP {#[iij---project-3]-adding-data-to-iyp}

Start a local IYP instance and add your favorite dataset to IYP. This would connect the imported dataset with the 60+ datasets already integrated into IYP, hence enabling new analysis. See [IYP documentation for adding new datasets](https://github.com/InternetHealthReport/internet-yellow-pages/tree/main/documentation#importing-a-new-dataset).

#### \[IIJ \- Project 3\] Web centralization {#[iij---project-3]-web-centralization}

* Reproduce (and extend if possible) key results from this recent study on web centralization:   
  [https://cs.stanford.edu/\~gakiwate/papers/sigcomm25-centralization.pdf](https://cs.stanford.edu/~gakiwate/papers/sigcomm25-centralization.pdf)   
* Main datasets are available in IYP (CRuX, DNS, BGP) with the exception of TLS

## 

## **Reverse Traceroute** {#reverse-traceroute}

### **Description** {#description-4}

Traceroute shows the path from a server to a client. Reverse Traceroute (RevTr) extends that visibility by measuring the path back from the client to the server. Because M-Lab servers cannot initiate traceroutes from the client side, RevTr reconstructs reverse paths using a combination of techniques. The details are described in our [blog post,](https://docs.google.com/document/u/1/d/1ObIiNmgIvm_vIWUduvIAtLZvv1Yox6dmTOa8AXH04_0/edit) which also explains how to access and use the dataset.

RevTr is integrated with M-Lab, and about 25% of NDT speed tests now include reverse traceroute measurements alongside. The results are publicly available in BigQuery, providing Internet-scale visibility into reverse paths and enabling studies of asymmetry, interconnection, and coverage.

### **Project Ideas** {#project-ideas-3}

#### \[RevTr \- Project 1\] General Study {#[revtr---project-1]-general-study}

* **Asymmetry analysis:** Using the notebook we shared as part of the blog post, identify cases of severe path asymmetry. How do these affect performance (e.g., by comparing with other measurements from the same city to the same site)? Are the asymmetries persistent? Could faster routes exist, (e.g., by using PeeringDB as a proxy for PoP locations while keeping the same AS path)?  
* **Coverage gaps:** Find parts of the network with very low response rates and suggest new Reverse Traceroute sources that could improve coverage.  
* **Visualization:** Design new ways to visualize forward and reverse paths at scale.

#### 

#### \[RevTr \- Project 2\] WeHeY Integration with RevTr {#[revtr---project-2]-wehey-integration-with-revtr}

[WeHeY](https://nal-epfl.github.io/WeHeY/) is a system for diagnosing whether an ISP is shaping or throttling traffic. The key idea is to compare performance to two different servers: if both tests share the same access link but diverge upstream, then differences in performance can reveal throttling/shaping inside the ISP.

For this to work, WeHeY needs two guarantees:

1. **Overlap at the client side.** Both tests must share the same path through the client’s ISP, so any differences can be attributed to that network.  
2. **Divergence upstream.** Beyond the ISP, the tests should be split into different paths, so that comparisons isolate the ISP’s influence.

The challenge is that with forward traceroutes alone, it is often unclear whether server pairs truly meet these conditions. Paths may look disjoint but still overlap in the reverse path.

**Project idea:** Use RevTr data to improve WeHeY’s precision and server selection. Reverse visibility can:

* **Reveal hidden overlaps** by showing that two candidate servers share more of the upstream path than expected, avoiding false positives.  
* **Confirm clean divergence** by verifying that beyond the ISP boundary, the reverse paths split as intended.  
* **Enable smarter server selection** by choosing pairs that truly only share the client’s ISP, maximizing the diagnostic power of each comparison.

Participants could quantify how often RevTr changes the overlap/divergence picture, and test whether these insights improve WeHeY’s accuracy at scale.

#### 

#### \[RevTr \- Project 3\] Poiroot Coverage with RevTr {#[revtr---project-3]-poiroot-coverage-with-revtr}

Poiroot is a system for attributing BGP path changes to the AS that caused them. Suppose traffic from AS A to a destination used to follow one sequence of ASes (the **OldPath**) and now follows a different sequence (the **NewPath**). Poiroot’s goal is to figure out which AS was responsible for that change.

To do this, Poiroot cannot rely only on the end-to-end OldPath and NewPath. It also needs to know:

1. **The new paths used by each AS that was on the OldPath.**

    *Example:* If the OldPath was A → X → Y → Z → Dest and X disappears from the NewPath, Poiroot needs to know: *where does X now send traffic toward the destination?*

2. **The old paths used by each AS that is on the NewPath.**

    *Example:* If the NewPath is A → W → Y → Z → Dest and W was not in the OldPath, Poiroot needs to know: *before this change, how did W reach the destination?*

Without this supporting information, attribution is ambiguous. Just knowing that the path changed from A → X → Y → Z → Dest to A → W → Y → Z → Dest doesn’t tell us who acted.

* If **X’s new path** shows that X still sends traffic to Y, then the change must have happened upstream at A (choosing W instead of X).  
* If **X’s new path** shows that X no longer sends to Y, then A’s change may have been induced by the change at X.  
* If **W’s old path** shows that W previously already sent through Y, then the change must have happened upstream at A (choosing W instead of X).  
* If W’s old path shows that W previously did not send through Y, then the change at W may have attracted A’s traffic.

In other words, the “before” and “after” paths of the ASes that join or leave the end-to-end path provide the crucial evidence for whether the decision was made by the source, the departing AS, or the newly added AS. Poiroot uses these extra views to isolate the specific AS responsible for the path change.

**Project idea:** Evaluate how much RevTr helps fill in these gaps. Reverse Traceroute expands visibility into return paths from many vantage points, which may capture the “before” and “after” routes that Poiroot needs. Hackathon participants could:

* Measure how often RevTr provides the additional paths required for (1) and (2).  
* Quantify how attribution success rates improve with RevTr data.  
* Identify where coverage remains insufficient and propose where new RevTr sources would add the most value.  
* Characterize the prevalence of induced path changes.

