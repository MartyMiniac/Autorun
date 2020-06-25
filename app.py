from flask import *
from getgit import get
import check
import getoutput
import json
import shutil
import os

app=Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        regno = request.form['regno']
        url = request.form['url']
        js=get.clone(regno,url)
        print(js)

        #js=getoutput.output(check.runmain(path))
        #print(json.dumps(js, indent=4))
        return js

    else:
        return render_template('index.html')

@app.route('/wait', methods=['GET'])
def wait():
    return render_template('wait.html')

@app.route('/output', methods=['POST'])
def output():
    print(json.dumps(request.json,indent=4))
    js=request.json
    msg=check.checkapi(js['code'],js['ext'])
    temp={}
    temp['name']=js['name']
    temp['msg']=msg
    return temp


if __name__ == "__main__":
    app.run()