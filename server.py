from flask import Flask, redirect, url_for, request, render_template, request
from modules.banner import bstring, print_banner_server
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

# flask.cli.show_server_banner = lambda *args: None # disable flask app default messages

# if args.verbose is False:
#     log = logging.getLogger('werkzeug')
#     log.setLevel(logging.ERROR)

app = Flask(__name__)

# @app.route("/", methods=["POST", "GET"])
# def index():
    
#     error = None
#     code = None
#     if request.method == "POST":
#         # current_date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
#         channel_id = request.form['channel']
#         time = request.form['sleep']
#         message = request.form['message']
#         unlimited1 = request.form.get('unlimited-id1') # returns None or 'on'
#         unlimited2 = request.form.get('unlimited-id2') # returns None or 'on'
#         unlimited3 = request.form.get('unlimited-id3') # returns None or 'on'
#         mode = request.form.get('mode1')

#         # def check_mode(x):
#         #     if request.form['submit_btn'] == 'Start%s' % x:
                

#         if request.form.get['submit_btn'] == 'Start1':
#             print('mode1')
#         elif request.form.get['submit_btn'] == 'Start2':
#             print('mode2')
#         elif request.form['submit_btn'] == 'Start3':
#             print('mode3')
#         elif request.form['submit_btn'] == 'Start4':
#             print('mode4')
#         elif request.form['submit_btn'] == 'Start5':
#             print('mode5')
#         elif request.form['submit_btn'] == 'Start6':
#             print('mode6')

        # print('\n', mode, '\n')

        # if unlimited == 'on' :
        #     unlimited_run = True
        # else:
        #     unlimited_run = False
            # message_count = request.form['d']

        # Catch errors
        # if unlimited_run == False:
        #     if channel_id == '' or message == '' or message_count == '':
        #         print(bstring.INFO, "Empty input error!")
        #         error = "Empty imput. Use brain!"
        #         return render_template('/index.html', error=error) 
        # elif unlimited_run == True:
        #     if channel_id == '' or message == '':
        #         print(bstring.INFO, "Empty input error!")
        #         error = "Empty imput. Use brain!"
        #         return render_template('/index.html', error=error)
        
        # render_template('/redirect.html', error='st')
        # print(bstring.INFO, "Launching DSE...\n")
        # Set up the dse.py command
        # code = 'python3 dse.py -c ' + channel_id 
        # if mode == 'mode1':
        #     code = code + ' -m "' + message +  '"' + ' -md 1 '
        # elif mode == 'mode2':
        #     code = code + ' -i "' + image +  '"' + ' -md 2 '
        # else:
        #     code = code + ' -m "' + message +  '"' + ' -i "' + image +  '"' + ' -md 3 '

        # if unlimited_run == True:
        #     code = code + ' -u'
        # elif message_count != '':
        #     code = code + ' -n ' + message_count
        

        # if time != '':
        #     code = code + ' -t ' + time

    #     code='jd'
    #     render_template('/redirect.html', error=code)

    #     os.system(r'"%s"' % code) 
    #     return render_template('/redirect.html', error=code) # Not an error, just sending cmd to redirect.html 

    # else:
    #     print(bstring.INFO, 'DSE panel loaded!')
    #     return render_template('/index.html') 


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # Setup variables
        channel_id=request.form['channel']
        # server_id=request.form['server']
        # user_id=request.form['user']
        # message=request.form['message']
        # image_path=request.form['image']
        # message_count=request.form['messagecount']
        # unlimited=request.form.get('unlimited') # returns None or 'on'
        # time_sleep=request.form['sleep']

        # 300IQ form value picker
        data = request.form['submit_btn']
        for i in range(1,6):
            if 'Start%s' % i in data:
                mode = i

        print(bstring.INFO,mode)

        if mode == 1 and channel_id == '':
            print(bstring.INFO, 'Empty input error!')
            error = 'Empty input error. Use brain!'
            return render_template('index.html', error=error)
        else:
            return render_template('redirect.html', error='ok')

        # Setup dse command
        # cmd = 'python3 dse.py'
        # if mode == 1:
        #     if channel_id == '' or message_count == '':
        #         print(bstring.INFO, "Empty input error!")
        #         error = "Empty input. Use brain!"
        #         return render_template('/index.html', error=error)
        #     cmd = cmd + ' -c ' + channel_id + ' -md ' + mode + ' -m "' + message + '"'

        # elif mode == 2:
        #     if channel_id  == '' or image_path == '':
        #         print(bstring.INFO, "Empty input error!")
        #         error = "Empty input. Use brain!"
        #         return render_template('/index.html', error=error)
        #     cmd = cmd + ' -c ' + channel_id + ' -md ' + mode + ' -i "' + image_path + '"' 

        # elif mode == 3:
        #     if channel_id == '' or message_count == '' or image_path == '':
        #         print(bstring.INFO, "Empty input error!")
        #         error = "Empty input. Use brain!"
        #         return render_template('/index.html', error=error)
        #     cmd = cmd + ' -c ' + channel_id + ' -md ' + mode + ' -i "' + image_path + '"' + ' -m "' + message + '"'

        # elif mode == 4:
        #     if server_id == '':
        #         print(bstring.INFO, "Empty input error!")
        #         error = "Empty input. Use brain!"
        #         return render_template('/index.html', error=error)
        #     cmd = cmd + ' -s ' + server_id + ' -md ' + mode 

        # elif mode == 5:
        #     if server_id == '':
        #         print(bstring.INFO, "Empty input error!")
        #         error = "Empty input. Use brain!"
        #         return render_template('/index.html', error=error)
        #     cmd = cmd + ' -s ' + server_id + ' -md ' + mode 

        # elif mode == 6:
        #     if user_id == '':
        #         print(bstring.INFO, "Empty input error!")
        #         error = "Empty input. Use brain!"
        #         return render_template('/index.html', error=error)
        #     cmd = cmd + ' -f ' + server_id + ' -md ' + mode 

        # for x in range(1,3):
        #     if x in mode:
        #         if time_sleep is not None:
        #             cmd = cmd + ' -t ' + time_sleep
        #         if unlimited == 'on':
        #             cmd = cmd + ' -u'
        #         elif unlimited is None:
        #             cmd = cmd + ' -n ' + message_count
        #         else:
        #             print(bstring.ERROR, 'Empty option error!')
        #             error = 'Choose at least one option!'
        #             return render_template('/index.html', error=error)
                    
        # os.system('start ' + cmd) # Opens cmd with command on Windows
        # render_template('/redirect.html', error=mode)
        return render_template('index.html')
    
    else:
        print(bstring.INFO, 'DSE panel loaded!')
        return render_template('index.html')

if __name__ == '__main__':
    print_banner_server()
    print(bstring.INFO, "Server started http://%s:%s" % (HOST_NAME,PORT))
    try:
        app.run(host=HOST_NAME, port=PORT)
    except KeyboardInterrupt:
        pass
        print(bstring.ERROR + "Server stopped!")
        app.stop()