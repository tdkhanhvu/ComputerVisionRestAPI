# author: Tran Doan Khanh Vu
# date: 2021-10-09
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
from flask import render_template

# Lite SQL DB
import sqlite3 as sql

class ComputerVision():
    """The core functions of the REST API to detect rectangles surrounding faces"""
    db = ""

    def __init__(self, db):
        self.db = db

    def create_table(self):
        """Create the table in this Database if not exists"""

        with sql.connect(self.db) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    ip VARCHAR,
                    timestamp TIMESTAMP
                );
            """)

    def write_record(self, req):
        """Write the timestamp and ip address of this request into the db"""

        with sql.connect(self.db) as connection:
            cur = connection.cursor()
            insert_sql = "INSERT INTO requests (ip, timestamp) values(?, ?)"
            data = (req.remote_addr, str(datetime.now(tz=None)))

            cur.execute(insert_sql, data)

            connection.commit()

    def convert_into_image(self, request):
        """Convert the image sent in this request into an Image object"""

        im_b64 = request.json["image"]
        img_bytes = base64.b64decode(im_b64.encode("utf-8"))
        
        return Image.open(io.BytesIO(img_bytes))

    def list_requests(self):
        """List all HTTP POST requests sent to this server"""

        with sql.connect(self.db) as connection:
            read_sql = "SELECT * FROM requests;"

            cur = connection.cursor()
            cur.execute(read_sql)

            data = cur.fetchall()
            df = pd.DataFrame(data, columns =["Id", "IP", "Timestamp"])
        
        return df

    def view_requests(self):
        """Return a web page displaying all HTTP POST requests sent to this server"""

        df = self.list_requests()

        return render_template(
            "view.html",
            tables=[df.to_html()],
            titles = ["Request"]
        )

    def recognize_face(self, request):
        """Send back coordinates of rectangles surrounding faces"""

        if not request.json or "image" not in request.json:
            return {"coordinates": []}
        
        self.write_record(request)

        img = self.convert_into_image(request)

        # PIL image object to numpy array
        arr = np.asarray(img)      
        print("Receive an image of shape:", arr.shape)

        coords = face_recognition.face_locations(arr)
        print("Return coordinates: ", coords)

        return {"coordinates": coords}
