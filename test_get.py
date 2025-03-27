import requests

app_id = 1  # Change this to the ID returned in Step 1
url = f'http://127.0.0.1:5000/get-app/{app_id}'

response = requests.get(url)
print(response.status_code)
print(response.json())
