from flask import Flask, redirect, render_template, request, session, url_for, Response


import json

import time
import subprocess
import os 
import sys


##settings 

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
app = Flask(__name__, static_url_path='')



os.chdir(dir_path)


########## serving functions

@app.route('/')
def index():
    
    return app.send_static_file('index.html')


##server start

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = False, port=23445)
