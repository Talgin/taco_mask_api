from typing import Union, Optional, List
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, Form, Response, status, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pandas import DataFrame as df
from sklearn import preprocessing

import pickle

from fastapi import APIRouter, Depends
from models import Result, User
from app.security import check_authentication_header

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/authorization/", dependencies=[Security(get_api_key)])
def result():
    return {'result': 'Success'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/test/function/")
def test_function(test_data: str = Form(...)):    
    return {"result": True, "message": test_data}