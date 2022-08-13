import requests
import json

def test():
    url = 'https://randommer.io/api/Card'
    r = requests.get(url, headers={'X-API-KEY':'438c6ba4be20466e919f22a437834658'})
    r1 = r.json()
    return r1

x = test()
with open('json_file.json', 'w') as f:
    json.dump(x, f, indent=2)