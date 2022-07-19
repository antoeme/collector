import requests

GET_TEMP = "http://127.0.0.1:5000/temp"  #url del server per la get delle temperature


response = requests.get(GET_TEMP)
print(response)
print(response.json())  



