import argparse
from cgitb import lookup
import enum
import requests
import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': 'AIzaSyC3V-YHo-ESvupSE-Ue1hdG_1gTX_rfFzQ',
}

data = '{urls: "https://www.rankwatch.com/blog/competitor-monitoring/"."https://www.rankwatch.com/blog/"}'


response = requests.post('https://acceleratedmobilepageurl.googleapis.com/v1/ampUrls:batchGet', headers=headers, data=data, verify=False)

