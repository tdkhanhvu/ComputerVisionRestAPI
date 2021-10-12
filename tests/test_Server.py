# author: Tran Doan Khanh Vu
# date: 2021-10-09

import os
import tempfile
import sys
import base64

from flask import Request

import pytest
from mockito import mock

sys.path.insert(1, os.path.join("src"))
from computervision import ComputerVision

@pytest.fixture
def cv():
    db_fd, db_path = tempfile.mkstemp()
    cv = ComputerVision(db_path)
    cv.create_table()

    yield cv

    os.close(db_fd)
    os.unlink(db_path)

def test_write_record(cv):
    req = mock({"remote_addr": "1.1.1.1"})
    cv.write_record(req)
    
    df = cv.list_requests()

    assert df.shape == (1,3)

def test_list_records(cv):
    df_before = cv.list_requests()
    req = mock({"remote_addr": "1.1.1.1"})
    cv.write_record(req)
    df_after = cv.list_requests()

    assert df_before.shape == (0,3)
    assert df_after.shape == (1,3)

def test_recognize_face_no_face(cv):
    img_path = "tests/sample_image_no_face.jpg"
    req = setup_recognize_face(img_path)
    
    result = cv.recognize_face(req)

    assert "coordinates" in result

    coords = result["coordinates"]

    assert len(coords) == 0

def test_recognize_face_1_face(cv):
    img_path = "tests/sample_image.jpg"
    req = setup_recognize_face(img_path)
    
    result = cv.recognize_face(req)

    assert "coordinates" in result

    coords = result["coordinates"]

    assert len(coords) == 1
    assert coords[0] == (172, 788, 726, 233)

def test_recognize_face_2_faces(cv):
    img_path = "tests/sample_image_couple_2.jpeg"
    req = setup_recognize_face(img_path)
    
    result = cv.recognize_face(req)

    assert "coordinates" in result

    coords = result["coordinates"]

    assert len(coords) == 2
    assert coords[0] == (440, 2148, 663, 1925)
    assert coords[1] == (217, 1083, 440, 860)

def setup_recognize_face(img_path):
    with open(img_path, "rb") as f:
        img_bytes = f.read()        
    
    image_file = base64.b64encode(img_bytes).decode("utf8")

    return mock({"remote_addr": "1.1.1.1", "json": {"image": image_file}})
