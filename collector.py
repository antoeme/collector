from flask import Flask,jsonify
import requests

GET_TEMP = "http://127.0.0.1:5000/temp"  #url del server per la get delle temperature
GET_STATUS_RELAYS = "http://127.0.0.1:5000/status"

app = Flask(__name__)

@app.route('/')
def helloworld():
    return jsonify({"about": " Helloworld !"})

# @app.route('/status_relays')
# def get_status():
#     response_status = requests.get(GET_STATUS_RELAYS)
#     #print(response_status)
#     return jsonify({"about" : response_status.json})

response = requests.get(GET_TEMP)
print(response)
print(response.json()) 
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=1000)




