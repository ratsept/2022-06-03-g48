from flask import Flask, request
from geopy import distance
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    f = open('index.html','r')
    return f.read()

@app.route("/trains")
def trains():
    r =requests.get('https://elron.ee/map_data.json?nocache=1654285204810')
    return r.text

@app.route("/closest_train")
def closest_train():
    args = request.args
    return args
