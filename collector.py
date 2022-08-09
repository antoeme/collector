import json
from flask import Flask,jsonify
import requests
from os import getenv

GET_TEMP = getenv("GET_TEMP") or "http://127.0.0.1:5000/temp"  #url del server per la get delle temperature
GET_STATUS_RELAYS = getenv("GET_STATUS_RELAYS") or "http://127.0.0.1:5001/status"

app = Flask(__name__)


@app.route('/')
def helloworld():
    return jsonify({"about": " Helloworld !"})

@app.route('/status_relays')
def get_status():
    response_status = requests.get(GET_STATUS_RELAYS)
    return jsonify(response_status.json())

@app.route('/temps')
def get_temps():
    response_temps = requests.get(GET_TEMP)
    print(response_temps) 
    return jsonify(response_temps.json()) #response.json è una lista, con jsonify diventa un json


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5002)




