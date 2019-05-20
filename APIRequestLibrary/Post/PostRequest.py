import requests
import json

BaseURL = "https://reqres.in/"

data = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post(BaseURL + "api/users", params=data)
print(response.status_code)

assert response.status_code == 201
print(json.dumps(response.json(), indent=4))
