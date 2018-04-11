import requests

url = "https://dog.ceo/api/breed/dingo/images/random"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "39205248-0441-47a8-bbce-e4516cc9d383"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)