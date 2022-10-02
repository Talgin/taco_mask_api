from typing import Union, Optional, List
from fastapi import FastAPI, Security
from fastapi import FastAPI, File, UploadFile, Form, Response, status, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from security import check_authentication_header
import numpy as np
import cv2
import pickle


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/authorization/", dependencies=[Security(check_authentication_header)])
def result():
    return {'result': 'Success'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/test/function/")
def test_function(test_data: str = Form(...)):    
    return {"result": True, "message": test_data}


@app.post("/detection/detect/", dependencies=[Security(check_authentication_header)])
async def detect_tacos(img: UploadFile = File(...)):
    if img is not None:
        # grab the uploaded image
        data = await img.read()
        name = img.filename
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        print('Image shape:', image.shape)
        # faces, landmarks = detector.detect(image, name, 0, settings.DETECTION_THRESHOLD)
    return {"result": True, "message": "Image processed successfully"}