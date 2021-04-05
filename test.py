import requests
from PIL import Image

file_name = 'test/0d61e4885d53a0abad1112c4edfa9fda.jpg'

with open(file_name, 'rb') as img:
    image = img.read()

resp = requests.post('http://dbc.my.to:8000', files={"image":image})

print(resp.json())