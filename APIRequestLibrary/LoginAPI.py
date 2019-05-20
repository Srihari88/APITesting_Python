import requests
import json
BaseURL = 'https://www.pitchvision.com/profile/login'

# Verify the the correct user details

response = requests.post(BaseURL, data={'username': 'daisy.dalia', 'password': 'dentrain'})

CorrectStatus = response.status_code
assert CorrectStatus == 200
print("Request URL", response.url, "Response code: ", CorrectStatus)

# print(response.json())
# print(json.dumps(response.json(), indent=4))
# Verify the the Incorrect user details

response = requests.post(BaseURL, data={'username': 'daisy.dalia', 'password': 'dentrain123'})

CorrectStatus = response.status_code
print("Response code: ", CorrectStatus)
assert CorrectStatus == 403

# print(response.json())
# print(json.dumps(response.json(), indent=4))
# Verify the the Incorrect user details

response = requests.post(BaseURL, data={'password': 'dentrain123'})

CorrectStatus = response.status_code
print("Request URL", response.url, "Response code: ", CorrectStatus)
# print(response.json())


# Verify the the Incorrect user details

response = requests.post(BaseURL, data={'username': 'daisy.dalia'})

CorrectStatus = response.status_code
print("Request URL", response.url, "Response code: ", CorrectStatus)
print(json.dumps(response.json(), indent=4))

print(response.text)
print(response.content)
print(response.headers)
