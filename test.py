import argparse
from cgitb import lookup
from distutils import config
import enum
from inspect import ArgSpec
import requests
import urllib3
import certifi
import configparser
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='amp',
                                         user='root',
                                         password='shikhar08')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

def main():
 parser = argparse.ArgumentParser()
 parser.add_argument("apikey", help="enter your api key")
 global args
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

if __name__ == "__main__":
    main()


