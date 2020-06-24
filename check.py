import os
import base64
import requests
import json
import time
#replace xxx in x-rapidapi-key with your own key

url = "https://judge0.p.rapidapi.com/submissions?base64_encoded=true"
headers = { 
    'x-rapidapi-host': 'judge0.p.rapidapi.com',
    'x-rapidapi-key': "xxx",
    'content-type': "application/json",
    'accept': "application/json"
    }
dis={}
dis['.c']=50
dis['.cpp']=54
dis['.cs']=51
dis['.exe']=44
dis['.java']=62
dis['.js']=63
dis['.kt']=78
dis['.m']=79
dis['.py']=71
dis['.rb']=72
dis['.rs']=73
dis['.vb']=84

def base_64_encoder(s):
    outp=base64.b64encode(bytes(s,'utf-8'))
    ans=str(outp)
    ans=ans[2:len(ans)-1]
    return ans

def check_c_string(base64_string,lang):
    payload = "{ \"language_id\": "+str(lang)+", \"source_code\": \"%s\\n\"}" % (base64_string)
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    js=json.loads(response.text)
    try:
        return js['token']
    except:
        return None




def runmain(dir):
    arr=os.listdir(dir)
    outp={}
    print(arr)
    for s in arr:
        ext=os.path.splitext(s)[1]
        print(ext)
        if ext in dis:
            langid=dis[ext]
            f=open(dir+'/'+s,'r')
            scode=f.read()
            b64=base_64_encoder(scode)
            token=check_c_string(b64,langid)
            outp[s]=get_output(token)
    return outp

def get_output(token):
    time.sleep(5)

    url = "https://judge0.p.rapidapi.com/submissions/"+token

    headers = {
        'x-rapidapi-host': "judge0.p.rapidapi.com",
        'x-rapidapi-key': "xxx"
        }

    response = requests.request("GET", url, headers=headers)

    return response.text