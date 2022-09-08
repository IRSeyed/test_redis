import redis, json, os
from flask import Flask, request, jsonify


app = Flask(__name__)
r = redis.from_url(os.environ['REDIS_URL'])

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    file = open('data.json', 'r')
    t = r.get('temp')
    h = r.get('hum')
    data = {'temp' : t, 'hum' : h }
    return jsonify(data)

@app.route('/getreq')
def get_req():
    variable = request.get_json()
    r.set('temp', variable['temp'])
    r.set('hume', variable['hum'])
    return 'ok'
