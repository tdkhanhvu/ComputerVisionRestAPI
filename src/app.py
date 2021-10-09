# base python imports
import io                
import base64                  
import logging

# image-related imports
import numpy as np
from PIL import Image

# Computer Vision library imports
import face_recognition

# Rest API library import
from flask import Flask, request, abort

app = Flask(__name__)
# app.logger.setLevel(logging.DEBUG)

@app.route('/recognizeFace', methods = ['POST'])
def recognize_face():  
    if not request.json or 'image' not in request.json: 
        abort(400)
             
    # convert base64 encoded string into bytes and PIL Image object
    im_b64 = request.json['image']
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))
    img = Image.open(io.BytesIO(img_bytes))

    # PIL image object to numpy array
    arr = np.asarray(img)      
    print('Receive an image of shape:', arr.shape)

    coords = face_recognition.face_locations(arr)[0]
    print('Return coordinates: ', coords)

    return {'coordinates': coords}
