import os
from flask import Flask, request, send_from_directory
from jinja2 import Markup, PackageLoader, Environment, FileSystemLoader, ChoiceLoader
dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
import subprocess
LISTENPORT = int(subprocess.Popen('for OPTS in $(ps ax | grep '+str(os.getpid())+');do echo $OPTS | grep -q  "\-\-listenport=" && echo $OPTS | cut -d = -f 2;done', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=256*1024*1024).communicate()[0].decode('utf8').replace('\n', ''))
app = Flask(__name__)

from File import bluePrint as fileBluePrint
app.register_blueprint(fileBluePrint)

@app.route("/")
def hello():
    return "Hello World!"

#if __name__ == "__main__":
#    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True, host='172.17.0.250', port=LISTENPORT)
