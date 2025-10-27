import requests

url ="https://api.restful-api.dev/objects"

result = requests.get(url)

if result.status_code == 200:
    data = result.json()

    print("API called successfully")
    for item in data[:3]:
        print("ID", item.get("id"))
        print("name", item.get("name"))

else:
    print("API failed")
