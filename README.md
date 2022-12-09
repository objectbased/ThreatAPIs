# ThreatAPIs
This Python script makes HTTP requests to multiple open source threat intelligence blocklists and aggregates the details together into dictionary objects for further searching.

# Requirements (Setup)

- Python 3.9+
- requests
- argparse
- re
```
pip3 install -r requirements.txt
```

## Usage
```
usage: threat_apis.py [-h] -i IOC [-t TYPE] [-s SOURCE]
options:
  -h, --help            show this help message and exit

required arguments:
  -i IOC, --ioc IOC            # query a indicator. #
  -t TYPE, --type TYPE         # indicator type (ip, domain, url) #
  -s SOURCE, --source SOURCE   # name of a given source/feed #
```
## Demos


# Troubleshooting
- If you are receiving errors, please look at the Issues queue and see if there is already an issue open.

- If you have a unique issue, please create a new Issue, and include the output of your terminal.
