# Rest API library import
from flask import Flask, request
from computervision import ComputerVision

DB = "face-recognition-requests.db"

cv = ComputerVision()
cv.create_table(DB)
app = Flask(__name__)

@app.route("/", methods= ["GET"])
def list_requests():
    return cv.list_requests()

@app.route("/recognizeFace", methods = ["POST"])
def recognize_face():
    """Send back coordinates of the rectangle surrounding the face"""

    return cv.recognize_face(request)
