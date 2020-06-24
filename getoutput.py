import json

def output(arr):
    dic={}
    for a,b in arr.items():
        js=json.loads(b)
        dic[a]=js['stdout']
    return dic