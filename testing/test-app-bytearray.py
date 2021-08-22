import requests
import base64

addr = 'http://localhost:5000/predict/base64'

path = 'test-img/test.png'

with open(path, "rb") as f:
    f_str = base64.b64encode(f.read())

response = requests.post(addr, json={'base64-img': f_str.decode("utf-8")})

data = response.json()

print(data)
print(f"Probability: {data['probability']}")
print(f"Class: {data['class_result']}")
