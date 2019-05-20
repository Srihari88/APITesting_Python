import requests
import json

BaseURL = "https://reqres.in/"

response = requests.post(BaseURL + "api/login", data={"email": "eve.holt@reqres.in", "password": "cityslicka"})
print(response.status_code)

assert response.status_code == 200
print(json.dumps(response.json(), indent=4))
