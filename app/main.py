from typing import Union, Optional, List
from fastapi import FastAPI, Security
from fastapi import FastAPI, File, UploadFile, Form, Response, status, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import security

import pickle


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/authorization/", dependencies=[Security(security.check_authentication_header)])
def result():
    return {'result': 'Success'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/test/function/")
def test_function(test_data: str = Form(...)):    
    return {"result": True, "message": test_data}

@app.post("/detection/detect/", dependencies=[Security(security.check_authentication_header)])
def detect_tacos(image: UploadFile(...)):
    return {"result": True, "message": "Image processed successfully"}