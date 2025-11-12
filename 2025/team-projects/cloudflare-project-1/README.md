# Internet outages: inbound & outbound measurements view

Radar provides a number of metrics that can help assess the occurrence and impact of a potential Internet disruption. (These include traffic metrics for HTTP requests, Netflows, and DNS; TCP resets & timeouts, bandwidth & latency, and announced IP address space.) However, these are largely all from a single platform. In order to corroborate observed disruptions, it would be helpful to have an aggregated view that includes metrics from other platforms. For example, for a given date or time period (last 24 hours):
* Has OONI seen an increased in failed measurements from the country/ASN?
* Has M-Lab seen a shift in the number of speed tests taken from the country/ASN, or a notable change in test results?
* Has IODA seen a change in their Active Probing or Telescope metrics?

## Proposed Project:
Build a publicly-accessible web-based dashboard that takes a country code or AS number and a date or time period (24h, 7d, etc) as input, and visualizes relevant metrics across providers. Can be on a single graph, or may be across per-metric graphs. Challenges likely include aggregation periods differing across providers, and how providers represent metric values (zero-to-max, absolute values, percentages, etc.)

## Hackathon Team Presentation
* [Internet outages: inbound & outbound measurements view](Group1_OneTimeseries_AllPlatforms.pdf)
