# Rest API library import
from flask import Flask, request
from src.computervision import ComputerVision

DB = "face-recognition-requests.db"

cv = ComputerVision(DB)
cv.create_table()
app = Flask(__name__)

@app.route("/", methods= ["GET"])
def view_requests():
    """View all requests sent to this REST API"""
    return cv.view_requests()

@app.route("/recognizeFace", methods = ["POST"])
def recognize_face():
    """Send back coordinates of the rectangle surrounding the face"""
    return cv.recognize_face(request)
