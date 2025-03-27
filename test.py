import requests

data = {
    "app_name": "Test App",
    "version": "1.0",
    "description": "Sample app"
}

res = requests.post("http://127.0.0.1:5000/add-app", json=data)

print(res.status_code)
print(res.json())
