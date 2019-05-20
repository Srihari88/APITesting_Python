import requests
import json

BaseURL = 'https://www.pitchvision.com/#/pvm/94689'

# Verify the the correct user details

response = requests.delete(BaseURL)

print(response.status_code)

