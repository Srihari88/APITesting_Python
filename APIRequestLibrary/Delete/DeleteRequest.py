import requests
import json

BaseURL = "https://reqres.in/"

response = requests.delete(BaseURL + "api/users/2")
print(response.status_code)

assert response.status_code == 204
#print(json.dumps(response.json(), indent=4))
print(response.url)
