# base python imports
import io
import base64                  
from datetime import datetime

import pandas as pd
import numpy as np

# image-related imports
from PIL import Image

# Computer Vision library imports
import face_recognition

# Rest API library import
from flask import Flask, request, abort, render_template

# Lite SQL DB
import sqlite3 as sql

DB = "face-recognition-requests.db"

def create_table(db):
    """Create the table in this Database if not exists"""

    with sql.connect(db) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                ip VARCHAR,
                timestamp TIMESTAMP
            );
        """)

def write_record(req, db=DB):
    """Write the timestamp and ip address of this request into the db"""

    with sql.connect(db) as connection:
        cur = connection.cursor()
        insert_sql = "INSERT INTO requests (ip, timestamp) values(?, ?)"
        data = (req.remote_addr, str(datetime.now(tz=None)))

        cur.execute(insert_sql, data)

        connection.commit()

def convert_into_image(request):
    """Convert the image sent in this request into an Image object"""

    im_b64 = request.json["image"]
    img_bytes = base64.b64decode(im_b64.encode("utf-8"))
    
    return Image.open(io.BytesIO(img_bytes))

create_table(DB)
app = Flask(__name__)

@app.route("/", methods= ["GET"])
def list_requests(db=DB):
    """List all requests sent to this server"""

    with sql.connect(db) as connection:
        read_sql = "SELECT * FROM requests;"

        cur = connection.cursor()
        cur.execute(read_sql)

        data = cur.fetchall()
        df = pd.DataFrame(data, columns =["Id", "IP", "Timestamp"])
        print(df.shape)

        return render_template(
            "view.html",
            tables=[df.to_html()],
            titles = ["Request"]
        )

@app.route("/recognizeFace", methods = ["POST"])
def recognize_face():
    """Send back coordinates of the rectangle surrounding the face"""

    if not request.json or "image" not in request.json:
        abort(400)
    
    write_record(request)

    img = convert_into_image(request)

    # PIL image object to numpy array
    arr = np.asarray(img)      
    print("Receive an image of shape:", arr.shape)

    coords = face_recognition.face_locations(arr)
    print("Return coordinates: ", coords)

    return {"coordinates": coords}
