import requests
import urllib3
import json
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

api_url = "http://127.0.0.1:8000/login"

login = {
    "login_id": "admin",
    "password": "Admin1234"
}

def main():
    try:
        response = requests.post(api_url, json.dumps(login), verify=False)
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()