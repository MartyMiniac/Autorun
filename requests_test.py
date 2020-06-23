import requests

url = "https://judge0.p.rapidapi.com/submissions"

payload = "{ \"language_id\": 50, \"source_code\": \"#include <stdio.h>\\n\\nint main(void) {\\n  char name[10];\\n  scanf(\\\"%s\\\", name);\\n  printf(\\\"hello %s\\\\n\\\", name);\\n  return 0;\\n}\", \"stdin\": \"world\"}"
headers = {
    'x-rapidapi-host': 'judge0.p.rapidapi.com',
    'x-rapidapi-key': "test",
    'content-type': "application/json",
    'accept': "application/json"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
