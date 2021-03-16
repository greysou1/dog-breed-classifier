import requests
encoded_file = open('test_examples/encoded_image.txt', 'r')
base64_string = encoded_file.read()
encoded_file.close()

resp = requests.post('http://dbc.my.to:8000', json={"image":base64_string})

print(resp.json())