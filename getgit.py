from git import Repo
import os
import json
import check
import javacompile

class get(object):
    def clone(name, url):
        dis={}
        dis['.c']=50
        dis['.cpp']=54
        dis['.CPP']=54
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
        abdir=os.path.abspath("gitrepo")
        dir=abdir+"/"+name+"/"
        try:
            Repo.clone_from(url, dir)
        except:
            print('repo already exists')
        arr=os.listdir(dir)
        dis2=[]
        for s in arr:
            ext=os.path.splitext(s)[1]
            if ext in dis:
                if ext == ".java":
                    js={}
                    js['name']=s
                    f=open(dir+s,'r')
                    js['code']=javacompile.main(f.read(),os.path.splitext(s)[0])
                    js['ext']=ext
                    dis2.append(js)
                else:
                    js={}
                    js['name']=s
                    f=open(dir+s, 'r')
                    js['code']=check.base_64_encoder(f.read())
                    js['ext']=ext
                    dis2.append(js)
                
        return json.dumps(dis2)