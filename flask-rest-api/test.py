import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "first vid", "likes": 1233, "views": 10233},
    {"name": "other vid", "likes": 24440, "views": 1999990},
    {"name": "heh vid", "likes": 14, "views": 1022300}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.delete(BASE + "video/0")
print(response)

response = requests.get(BASE + "video/2")
print(response.json())
