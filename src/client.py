# author: Tran Doan Khanh Vu
# date: 2021-10-09

"""Send an image to a Rest API in Python to get back the coordinates of boxes localizing faces

Usage: src/client.py --api=<api> --img_path=<img_path>

Options:
--api=<api>              The API End Point
--img_path=<img_path>    The path to the image to be processed
"""

import base64
import json                    
from docopt import docopt

import requests

opt = docopt(__doc__)

def load_image(img_path):
    """Load an image from a path"""
    with open(img_path, "rb") as f:
        img_bytes = f.read()        
    
    return base64.b64encode(img_bytes).decode("utf8")

def send_request(api, image_file):
    """Send this image to this API End Point"""
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    
    payload = json.dumps({"image": image_file, "other_key": "value"})
    
    return requests.post(api, data=payload, headers=headers)

def proces_result(response):
    """Process the response sent by the server"""
    try:
        data = response.json()     
        print("Response:", data)                
    except requests.exceptions.RequestException:
        print("Error:", response.text)

def main(api, img_path):
    """Send an image to a REST API using HTTP POST"""
    print("API:", api, ", Image path:", img_path)

    image_file = load_image(img_path)
    response = send_request(api, image_file)
    proces_result(response)

if __name__ == "__main__":
    main(opt["--api"], opt["--img_path"])