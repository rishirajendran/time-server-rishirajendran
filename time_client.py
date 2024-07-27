import requests

server = "http://127.0.0.1:5000"

out_json = {'date': "10/21/1999", 'units': "years"}
r = requests.post(server+"/age", json=out_json)
print(r.status_code)
print(r.text)

x = r.json()
print(x)
