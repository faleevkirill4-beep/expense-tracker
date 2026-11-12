import json 
import requests

url ="https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)

    with open("photo.json","w") as f:
        json.dump(data,f,ensure_ascii=False,indent = 2)

    