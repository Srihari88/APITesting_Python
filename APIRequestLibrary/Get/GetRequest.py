import requests
import json

BaseURL = "https://reqres.in/"

response = requests.get(BaseURL + "api/users?page=2")
print(response.status_code)

# Verify the status code

assert response.status_code == 200

# print(response.json())
print(json.dumps(response.json(), indent=4))
