# base python imports
import io
import base64                  
from datetime import datetime

# image-related imports
import pandas as pd
import numpy as np
from PIL import Image

# Computer Vision library imports
import face_recognition

# Rest API library import
from flask import Flask, request, abort, render_template

# Lite SQL DB
import sqlite3 as sql

DB = 'face-recognition-requests.db'

def connect_db():
    with sql.connect(DB) as connection:
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
    with sql.connect(DB) as connection:
        cur = connection.cursor()
        insert_sql = 'INSERT INTO requests (ip, timestamp) values(?, ?)'
        data = (req.remote_addr, str(datetime.now(tz=None)))

        cur.execute(insert_sql, data)

        connection.commit()


@app.route('/', methods= ['GET'])
def list_requests():
    with sql.connect(DB) as connection:
        read_sql = 'SELECT * FROM requests;'

        cur = connection.cursor()
        cur.execute(read_sql)

        data = cur.fetchall()
        df = pd.DataFrame(data, columns =['Id', 'IP', 'Timestamp'])
        print(df.shape)

        return render_template('view.html', tables=[df.to_html(classes='Vu')],
    titles = ['Request'])


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
