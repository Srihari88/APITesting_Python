import requests
import json
import unittest


class MyAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global Base_Url
        Base_Url = "https://www.pitchvision.com"

    def test_A_Login(self):
        response = requests.post(Base_Url + "/profile/login", data={'username': 'daisy.dalia', 'password': 'dentrain'})
        print(response.status_code)
        print(response.url)
        assert response.status_code == 200

    def test_B_Content(self):
        response = requests.get(Base_Url + "/profile/login")
        print(response.content)

    @classmethod
    def tearDownClass(cls):
        print(" Close connections")


if __name__ == '__main__':
    unittest.main()
