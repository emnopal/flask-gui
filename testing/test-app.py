import requests

addr = 'http://localhost:5000/predict/image'

path = 'test-img/test.png'

response = requests.post(addr, json={'img': path})

data = response.json()

print(f"Probability: {data['probability']}")
print(f"Class: {data['class_result']}")
