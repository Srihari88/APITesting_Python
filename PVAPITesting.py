import requests
import json

BaseURL = 'https://www.pitchvision.com'

# Profile verification


response = requests.post(BaseURL+"/profile/login", data={'username': 'daisy.dalia', 'password': 'dentrain'})

CorrectStatus = response.status_code
assert CorrectStatus == 200
print("Request URL", response.url, "Response code: ", CorrectStatus)

response = requests.get(BaseURL + "/profile/details/14009")
print(json.dumps(response.json(), indent=4))

print(response.status_code)

CorrectStatus = response.status_code
assert CorrectStatus == 200

# Sessions verifications

response = requests.get(BaseURL + "/profile/session")
print(json.dumps(response.json(), indent=4))

print(response.status_code)

CorrectStatus = response.status_code
assert CorrectStatus == 200
