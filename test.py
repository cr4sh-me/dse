import requests

channelID = 1047596177241145375
headers = {"authorization": "NzAxMTYyNTAwMzM0NTUxMTEx.GCOla9.X1_O7Tg6athNFPdAR9S5xf7Yp4brvSidHcl58M"}
file_path = './images/myimg.png'
# files_a = {'file': (file_path, open(file_path, 'rb'))}
with open(file_path, "rb") as f1:
    files_a = [f1]
message = {
    'content': "Test"
}



for i in range(5):
    req = requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", data=message, headers=headers, files=files_a)
    print(req)