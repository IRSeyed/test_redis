import redis, json, os
from flask import Flask, request, jsonify


app = Flask(__name__)
r = redis.Redis.from_url('redis://red-cccr2omn6mpkorrftm60:6379')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    t = r.get('temp')
    h = r.get('hum')
    print(t, h)
    data = {'temp' : t, 'hum' : h }
    return jsonify(data)

@app.route('/getreq')
def get_req():
    variable = request.get_json()
    r.set('temp', variable['temp'])
    r.set('hume', variable['hum'])
    return 'ok'
