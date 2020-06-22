from flask import *
from getgit import get
import check
import getoutput
import json

app=Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        regno = request.form['regno']
        url = request.form['url']
        js=getoutput.output(check.runmain(get.clone(regno,url),regno))
        return render_template('output.html', js=js, regno=regno)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()