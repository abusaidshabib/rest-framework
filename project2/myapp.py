import requests
import json

URL = "http://localhost:8000/student/"

data = {
    'name': 'Sonam',
    'roll': 101,
    'city':'Ranchi'
}

json_data = json.dumps(data)
req = requests.post(url=URL, data=json_data)

if req.status_code == 200:
    data = req.json()
    print(data)
else:
    print(f"Request failed with status code {req.status_code}")