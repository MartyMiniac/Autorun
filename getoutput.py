import os

def output(dir):    
    arr=os.listdir(dir)
    dic={}
    for s in arr:
        f=open(dir+'\\'+s,'r')
        val=f.readlines()
        dic[s]=val
    return dic