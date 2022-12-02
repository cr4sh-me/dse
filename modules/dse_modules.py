# Took & modified some code from https://github.com/CryonicsX/Discord-Spammer
import time
import requests
from modules.banner import bstring

def send_message(token, channelID, message, useragent, proxies, iteration, limit, sleep_time):
    data = {"content": message}
    headers = {"authorization": token , "User-Agent" : useragent , "tts" : "false"}
    proxies = {"http" : proxies}

    try:
        req = requests.post(f"https://discordapp.com/api/v9/channels/{channelID}/messages" , data=data , headers=headers , proxies=proxies)
    except Exception as err:
        print(bstring.ERROR, "ERROR:", err)
    if req.status_code == 200:
        if limit == 0:
            print("\r" + bstring.INFO, "Sent message - {}".format(iteration))
        else:
            print("\r" + bstring.INFO, "Sent message - {}/{}".format(iteration, limit))
        time.sleep(sleep_time)
    else:
        print(bstring.ERROR,"Couldn't send message!", req.json())

def join_server(token, guildid, useragent, proxies):
	headers = {"content-type": "false",	"authorization": token , "User-Agent" : useragent}
	proxies = {"http" : proxies}
	try:
		req = requests.post(f"https://discordapp.com/api/v10/invite/{guildid}" , headers=headers , proxies=proxies)
	except Exception as err:
		print(bstring.ERROR, "ERROR:", err)
	if req.status_code == 204:
		print(bstring.INFO, "Joined server!")
	else:
		print(bstring.ERROR,"Couldn't join server!", req.json())

def leave_server(token, guildid, useragent, proxies):
	headers = {"content-type": "false",	"authorization": token , "User-Agent" : useragent}
	proxies = {"http" : proxies}
	try:
		req = requests.delete(f"https://discordapp.com/api/v10/invite/{guildid}" , headers=headers , proxies=proxies)
	except Exception as err:
		print(bstring.ERROR, "ERROR:", err)
	if req.status_code == 204:
		print(bstring.INFO, "Left server!")
	else:
		print(bstring.ERROR,"Couldn't leave server!", req.json())

def friend_request(token, userid, userAgent, proxies):
	headers = {"authorization": token , "User-Agent" : userAgent}
	proxies = {"http" : proxies}
	try:
		req = requests.put(f"https://discordapp.com/api/v10/users/@me/relationships/{userid}" , headers=headers , proxies=proxies)
	except Exception as err:
		print(bstring.ERROR, "ERROR:", err)
	if req.status_code == 204:
		print(bstring.INFO, "Friend request sent!")
	else:
		print(bstring.ERROR,"Couldn't send friend request!", req.json())