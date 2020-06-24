from git import Repo
import os
class get(object):
    def clone(name, url):
        abdir=os.path.abspath("gitrepo")
        dir=abdir+"\\"+name+"\\"
        try:
            Repo.clone_from(url, dir)
        except:
            print('repo already exists')
        return dir