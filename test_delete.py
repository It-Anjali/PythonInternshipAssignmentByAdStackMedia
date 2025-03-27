import requests

app_id = 1  # Replace with your actual app ID
url = f'http://127.0.0.1:5000/delete-app/{app_id}'

response = requests.delete(url)
print(response.status_code)
print(response.json())
