import requests
import urllib3
import json
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

api_url = "http://127.0.0.1:8000/search"

test = {
  "Query": {
    "limit": 150,
    "conditions": [
      {
        "column": "datetime",
        "operator": 5,
        "values": [
          "2023-05-31T10:00:00.000Z"
        ]
      },
      {
        "column": "event_type_id.code",
        "operator": 0,
        "values": [
          "4102"
        ]
      }
    ],
    "orders": [
      {
        "column": "datetime",
        "descending": False
      }
    ]
  }
}

def main():
    try:
        response = requests.post(api_url, headers={"aaa": "18db5f67d2df4ad0a8a2bd9a851f61c7"}, json=test, verify=False)
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()