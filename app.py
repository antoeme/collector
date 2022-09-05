
from flask import Flask,jsonify
import requests

from os import getenv
from dotenv import load_dotenv

from requests.auth import HTTPBasicAuth

GET_TEMP = getenv("GET_TEMP") #or "http://127.0.0.1:5000/temp"  #url del server per la get delle temperature
REL = getenv("REL") #or "http://127.0.0.1:5001/status"
PROVA = getenv("PROVA")
username = "daniele" or "antonio"
password = "Cisco123" or "Dtlab123"


app = Flask(__name__)

# load environment variables from '.env' file
load_dotenv()

@app.route('/prova', methods=['GET'] )   
def prova():
    response_status = requests.get(str(PROVA), auth=HTTPBasicAuth(username,password))
    return jsonify(response_status.json())


@app.route('/status_relays')
def get_status():
    response_status = requests.get(str(REL))
    print(response_status.json())
    print(str(REL))
    return jsonify(response_status.json())

@app.route('/temps')
def get_temps():
    response_temps = requests.get(str(GET_TEMP), auth=HTTPBasicAuth(username,password))
    print(response_temps.json())
    print(str(GET_TEMP))
    return jsonify(response_temps.json()) #response.json è una lista, con jsonify diventa un json


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True,port=5002)





