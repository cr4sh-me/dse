from flask import Flask, redirect, url_for, request, render_template, request
from modules.banner import bstring
import os
import argparse
import datetime
import subprocess
import flask.cli
import logging
import re

# pip3 install flask argparse

parser = argparse.ArgumentParser(description='DSE server help')
parser._action_groups.pop()
requiredNamed = parser.add_argument_group('required') ### REQUIRED ARGS ###
requiredNamed.add_argument(
        "-p",
        "--port",
        type=int,
        required=True,
        help=("Choose port for python http server. " +
            "All processes on that port will be killed! " + 
            "Example: -p 80"))
optionalNamed = parser.add_argument_group('optional') ### OPTIONAL ARGS ###
optionalNamed.add_argument(
        "-v",
        "--verbose",
        action='store_true',
        required=False,
        help=("Unhide default flask messages like GET/POST etc. " +
            "Example: -v"))

args = parser.parse_args()

HOST_NAME = "127.0.0.1"
PORT = (args.port)

flask.cli.show_server_banner = lambda *args: None # disable flask app default messages

if args.verbose is False:
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    
    error = None
    code = None
    if request.method == "POST":
        # current_date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
        xpath = request.form['a']
        xpath_channel = request.form['b']
        message = request.form['c']
        unlimited = request.form.get('e') # returns None or 'on'

        if unlimited == 'on' :
            unlimited_run = True
        else:
            unlimited_run = False
            message_count = request.form['d']

        # Catch errors
        if unlimited_run == False:
            if xpath == '' or message == '' or message_count == '':
                print(bstring.INFO, "Empty input error!")
                error = "Empty imput. Use brain!"
                return render_template('/index.html', error=error) 
        elif unlimited_run == True:
            if xpath == '' or message == '':
                print(bstring.INFO, "Empty input error!")
                error = "Empty imput. Use brain!"
                return render_template('/index.html', error=error)
        
        print(bstring.INFO, "Input ok, launching DSE!")
        # Set up the dse.py command
        code = 'python3 dse.py -x "' + xpath + '" -c "' + xpath_channel + '" -m "' + message +  '"'
        if unlimited_run == True:
            code = code + ' -u'
        else:
            code = code + ' -n ' + message_count

        # os.system(r'"%s"' % code) 
        # return render_template('/redirect.html', error=code) # Not an error, just sending cmd to redirect.html 

        def master_profile_update(inputs):
        # since input parameters are global inside the upper scope
        # i omit them from the arguments of lower nested function:
            def profile_update()
            #take updates and update the database 
            return "it worked"

        profile_update()
        #do maintenance processing now..
       

    


    else:
        print(bstring.INFO, 'Website opened!')
        return render_template('/index.html') 


if __name__ == '__main__':
    print(bstring.BOLD + "[ DSE Server v1.0 ]" + bstring.RESET)
    print(bstring.INFO, "Server started http://%s:%s" % (HOST_NAME,PORT))
    try:
        app.run(host=HOST_NAME, port=PORT)
    except KeyboardInterrupt:
        pass
        app.stop()
        print("\n" + "Server stopped")