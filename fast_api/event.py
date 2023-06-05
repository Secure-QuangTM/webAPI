import requests
import urllib3
import json
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

api_url = "http://127.0.0.1:8000/search"

def main():
    try:
        response = requests.post(api_url, json.dumps(login), verify=False)
        if response.status_code == 200:
            # data = response.headers["bs-session-id"]
            data = response.json()
            print(data)
            # return data
        else:
            print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()