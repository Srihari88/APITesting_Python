import requests
import json

BaseURL = "https://reqres.in/"
params = {'page': 3}

response = requests.get(BaseURL + "api/users", params=params)
# print(response.status_code)
# print(response.json())
print(json.dumps(response.json(), indent=4))


