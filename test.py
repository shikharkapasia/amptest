import argparse
from cgitb import lookup
from distutils import config
import enum
import requests
import urllib3
import certifi
import configparser

parser = argparse.ArgumentParser()
parser.add_argument("apikey", help="enter your api key")
args = parser.parse_args()
print(args.apikey)

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

config = configparser.ConfigParser()
config.read('config.ini')

host = config['googleapi']['host']
user = config['googleapi']['user']
apikey = config['googleapi']['apikey']

headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': args.apikey ,
}

data = '{urls: "https://www.rankwatch.com/blog/competitor-monitoring/"."https://www.rankwatch.com/blog/"}'


response = requests.post('https://acceleratedmobilepageurl.googleapis.com/v1/ampUrls:batchGet', headers=headers, data=data, verify=False)

