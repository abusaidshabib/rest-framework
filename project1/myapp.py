import requests
URL = "http://localhost:8000/student/1/"

req = requests.get(url = URL)

data = req.json()
print(data)

# pip install requests (this will help to install request)
# this will contact with the application and return api's data.