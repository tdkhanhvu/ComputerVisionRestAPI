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
from flask import Flask, request, render_template

# Lite SQL DB
import sqlite3 as sql


class ComputerVision():
    DB = ""


    def create_table(self, db):
        """Create the table in this Database if not exists"""
        self.DB = db

        with sql.connect(db) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS requests (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    ip VARCHAR,
                    timestamp TIMESTAMP
                );
            """)

    def write_record(self, req, db=None):
        """Write the timestamp and ip address of this request into the db"""

        if db is None:
            db = self.DB

        with sql.connect(db) as connection:
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

    def list_requests(self, db=None):
        """List all requests sent to this server"""

        if db is None:
            db = self.DB

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

    def recognize_face(self, request):
        """Send back coordinates of the rectangle surrounding the face"""

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
