import requests
import json
import re
import argparse
from bin import config

parser = argparse.ArgumentParser(
    description='This tool aggregates multiple different threat feeds and allows searching for various IoCs within these datasets.'
)

# Required arguments
required = parser.add_argument_group('required arguments')
required.add_argument("-i", "--ioc", help="query a indicator.", action="store", type=str, required=True)
required.add_argument("-t", "--type", help="indicator type (ip, domain, url)", action="store", type=str, required=False)
required.add_argument("-s", "--source", help=f"name of a given source/feed", action="store", type=str, required=False)

args = parser.parse_args()

build = []

def get_api_details():
    s = requests.Session()
    for index, url in enumerate(config.feeds['sources']):
        r = s.get(url['url'])
        data = r.text
        for line in data.split('\n'):
            line_exclude_filter = re.findall("^\#", line)
            if not line_exclude_filter:
                if config.feeds["sources"][index]['regex'] == "N/A":
                    build.append({"ioc": line.strip('\r'), "type": config.feeds["sources"][index]["type"][0], "source": config.feeds["sources"][index]["name"]})
                else:
                    regex_parser = re.findall(config.feeds["sources"][index]['regex'], line)
                    for line in regex_parser:
                        build.append({"ioc": line.strip('\r'), "type": config.feeds["sources"][index]["type"][0], "source": config.feeds["sources"][index]["name"]})

def main():
    get_api_details()
    for item in build:
        if (args.ioc).strip() in item["ioc"]:
            if args.type:
                if (args.type).strip() in item["type"]:
                    if args.source:
                        if (args.source).strip() in item["source"]:
                           print(item)
                    else:
                        print(item)       
            else:
                if args.source:
                    if (args.source).strip() in item["source"]:
                        print(item)
                    else:
                        print(item)
                else:
                    print(item)
  
# Call function
main()


