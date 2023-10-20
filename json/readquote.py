import urllib.request
import json 

q_url = 'https://zenquotes.io/api/today'
with urllib.request.urlopen(q_url) as url:
    data = json.loads(url.read().decode())
    print(data)