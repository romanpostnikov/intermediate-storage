from app import app, db
from app.models import Video
from flask import request
import os
import googleapiclient.discovery
import json

@app.route('/')
def index():
	return "Updated world"