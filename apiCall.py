import requests

url = "https://api.restful-api.dev/objects"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("API called successfully...")
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")    
