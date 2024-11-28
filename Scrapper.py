import requests
import argparse
import sys

# create a parser object
parser = argparse.ArgumentParser(description = "A web scrapper program")

# add argument
parser.add_argument('-u', '--url', type=str, help = "The argument is the webpage to be scraped")

# parse the arguments from standard input
args = parser.parse_args()

# make GET request
response = requests.get(args.url)

# print url
print(response.url)

# check status code for response received
# success code - 200
print(response.status_code)

# print content of request as text
print(response.text)