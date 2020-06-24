from flask import *
from getgit import get
import check
import getoutput
import json
import shutil

app=Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        regno = request.form['regno']
        url = request.form['url']
        path=get.clone(regno,url)
        js=getoutput.output(check.runmain(path))
        try:
            shutil.rmtree(path)
        except:
            print('Failed to delete the repo please delete it manually')
        return render_template('output.html', js=js, regno=regno)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)