import requests

url = "https://judge0.p.rapidapi.com/submissions"

payload = "{ \"language_id\": 50, \"source_code\": \"I2luY2x1ZGUgPHN0ZGlvLmg+CgppbnQgbWFpbih2b2lkKSB7CiAgY2hhciBu\\nYW1lWzEwXTsKICBzY2FuZigiJXMiLCBuYW1lKTsKICBwcmludGYoImhlbGxv\\nLCAlc1xuIiwgbmFtZSk7CiAgcmV0dXJuIDA7Cn0=\\n\", \"stdin\": \"d29ybGQ=\\n\"}"

headers = { 
    'x-rapidapi-host': 'judge0.p.rapidapi.com',
    'x-rapidapi-key': "339dba9922msh43e751b462b5016p1977d9jsna327bc002a18",
    'content-type': "application/json",
    'accept': "application/json"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
