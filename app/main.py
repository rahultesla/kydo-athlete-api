from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import UploadFile
from typing import Optional, Union
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():
    return {"status": "Working"}
