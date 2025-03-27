import requests

url = 'http://127.0.0.1:5000/add-app'
data = {
    "app_name": "My Cool App",
    "version": "1.0",
    "description": "Just testing the API."
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
