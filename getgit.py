from git import Repo
import os
class get(object):
    def clone(name, url):
        abdir=os.path.abspath("gitrepo")
        dir=abdir+"\\"+name+"\\"
        Repo.clone_from(url, dir)
        return dir