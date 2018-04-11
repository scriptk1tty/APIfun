import requests

url = "https://newsapi.org/v2/top-headlines"

querystring = {"country":"us","apiKey":"1594a48417854239bcdbd0d01fb5d86d"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "79a88315-e5ea-4696-9279-01fbdb54d69d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)