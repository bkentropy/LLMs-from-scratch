import urllib.request
import json

url = "http://localhost:1234/v1/chat/completions"
headers = {
    "Content-Type": "application/json"
}
data = {
    "model": "openhermes-2.5-mistral-7b",
    "messages": [
        {"role": "system", "content": "Always answer in rhymes. Today is Thursday"},
        {"role": "user", "content": "What day is it today?"}
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": False
}

# Convert the data dictionary to a JSON string
data_json = json.dumps(data).encode('utf-8')

# Create the request
req = urllib.request.Request(url, data=data_json, headers=headers, method="POST")

# Send the request and read the response
try:
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print("Response:", response_data)
except urllib.error.HTTPError as e:
    print("HTTPError:", e.code, e.reason)
except urllib.error.URLError as e:
    print("URLError:", e.reason)
