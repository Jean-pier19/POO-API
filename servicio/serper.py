import http.client
import json

def serper():
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
  "q": "apple inc"
    })
    headers = {
  'X-API-KEY': '933430550ae034084404bd8b1943d5d5dc6d1329',
  'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))