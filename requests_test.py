import requests

url = "https://judge0.p.rapidapi.com/submissions?base64_encoded=true"
base64 = "I2luY2x1ZGUgPHN0ZGlvLmg+CmludCBtYWluKCkgewogICAvLyBwcmludGYoKSBkaXNwbGF5cyB0aGUgc3RyaW5nIGluc2lkZSBxdW90YXRpb24KICAgcHJpbnRmKCJIZWxsbywgV29ybGQhIik7CiAgIHJldHVybiAwOwp9"

payload = "{ \"language_id\": 50, \"source_code\": \"%s\\n\", \"stdin\": \"d29ybGQ=\\n\"}" % (base64)

headers = { 
    'x-rapidapi-host': 'judge0.p.rapidapi.com',
    'x-rapidapi-key': "xxx",
    'content-type': "application/json",
    'accept': "application/json"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
