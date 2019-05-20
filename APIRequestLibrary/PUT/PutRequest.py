import requests
import json

BaseURL = "https://reqres.in/"

data = {
    "name": "morpheus",
    "job": "zion resident"
}

response = requests.put(BaseURL + "api/users", params=data)
print(response.status_code)

assert response.status_code == 200
print(json.dumps(response.json(), indent=4))
