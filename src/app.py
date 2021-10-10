# base python imports
import io                
import base64                  
from datetime import datetime

# image-related imports
import numpy as np
from PIL import Image

# Computer Vision library imports
import face_recognition

# Rest API library import
from flask import Flask, request, abort

# Lite SQL DB
import sqlite3 as sql

def connect_db():
    connection = sql.connect('face-recognition-requests.db')

    connection.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ip VARCHAR,
            timestamp TIMESTAMP
        );
    """)

connect_db()
app = Flask(__name__)

def write_record(req):
    with sql.connect('face-recognition-requests.db') as connection:
        insert_sql = 'INSERT INTO requests (ip, timestamp) values(?, ?)'
        data = (req.remote_addr, str(datetime.now(tz=None)))

        connection.execute(insert_sql, data)

@app.route('/recognizeFace', methods = ['POST'])
def recognize_face():  
    if not request.json or 'image' not in request.json:
        abort(400)
    
    write_record(request)
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
