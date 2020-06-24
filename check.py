import os
import base64
import requests

url = "https://judge0.p.rapidapi.com/submissions?base64_encoded=true"
headers = { 
    'x-rapidapi-host': 'judge0.p.rapidapi.com',
    'x-rapidapi-key': "xxx",
    'content-type': "application/json",
    'accept': "application/json"
    }


def base_64_encoder(s):
    outp=base64.b64encode(bytes(s,'utf-8'))
    ans=str(outp)
    ans=ans[2:len(ans)-1]
    return ans

def check_c_string(base64_string):
    payload = "{ \"language_id\": 50, \"source_code\": \"%s\\n\", \"stdin\": \"d29ybGQ=\\n\"}" % (base64_string)
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text




def runmain(dir,name):
    arr=os.listdir(dir)
    abdir=os.path.abspath("app.py")
    abdir=str(abdir)[0:len(abdir)-6]
    abdir=abdir+'outputs/'+name+'/'
    os.system('mkdir "'+abdir+'"')
        
    for s in arr:
        pt=os.path.splitext(s)
        ext=os.path.splitext(s)[1]
        if ext == ".java":
            runjava(dir+'/'+s,pt[0],abdir,name)
        
        if ext == ".cpp":
            runcpp(dir+'/'+s,pt[0],abdir,name)
        
        if ext == ".c":
            runc(dir+'/'+s,pt[0],abdir,name)

        if ext == ".py":
            runpy(dir+'/'+s,pt[0],abdir,name)
    return abdir

def runjava(dir, name, abdir, sname):
    os.system('java "'+dir+'" > "'+abdir+name+'.txt"')

def runcpp(dir, name, abdir, sname):
    os.system('g++ -o main "'+dir+'"')
    os.system('./main > "'+abdir+name+'.txt"')

def runc(dir, name, abdir, sname):
    os.system('g++ -o main "'+dir+'"')
    os.system('./main > "'+abdir+name+'.txt"')

def runpy(dir, name, abdir, sname):
    os.system('py "'+dir+'" > "'+abdir+name+'.txt"')