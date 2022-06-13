import json
from flaskapi import Flask, request, jsonify
import argparse
import test


app = Flask(__name__)

def ampurl():
    headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': test.args.apikey ,
}


@app.route('https://acceleratedmobilepageurl.googleapis.com/v1/ampUrls:batchGet', methods=['GET', 'POST'])
def create_record():
    record = json.loads(request.data)
    return jsonify(record)
