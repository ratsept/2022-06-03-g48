from flask import Flask, request, Response, send_file
from geopy import distance
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    f = open('index.html','r')
    return f.read()

@app.route("/service-worker.js")
def service_worker():
    f = open('service-worker.js','r')
    return Response(f.read(), mimetype='text/javascript')

@app.route("/train.png")
def train():
    return send_file('train.png', mimetype='image/png')

@app.route("/trains")
def trains():
    r =requests.get('https://elron.ee/map_data.json?nocache=1654285204810')
    return r.text

@app.route("/closest_train")
def closest_train():
    args = request.args
    r = json.loads(requests.get('https://elron.ee/map_data.json?nocache=1654285204810').text)
    min_d = float("inf")
    #d = distance.distance((args["lat"],args["lon"]),(r["data"][0]["latitude"],r["data"][0]["longitude"])).km
    for train in r["data"]:
        d = distance.distance((args["lat"],args["lon"]),(train["latitude"],train["longitude"])).km
        if d < min_d:
            min_d = d
    return str(min_d)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
