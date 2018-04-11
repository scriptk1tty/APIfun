import requests

url = "http://api.openweathermap.org/data/2.5/forecast"

querystring = {"id":"5866583","APPID":"6b5b441a4d7496d1f0389a9045f594dc"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "d19a66c9-4766-497d-99b5-d2738a927f68"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)