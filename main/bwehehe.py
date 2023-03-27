import time

import requests


def sendmsg(msg, id):
    payload = {
        'content': f"{msg}"
    }

    header = {
        'authorization': 'almost doxxed myself'
    }

    r = requests.post(f"https://discord.com//api/v9/channels/{id}/messages", data=payload, headers=header)
    if r.status_code == 401:
        print("failed to send message")
    else:
        print(f"\"{msg}\" sent.")


file = open("file.txt", "r")
chnlId = input("input channel id: ")
alist = file.read().split(". ")
for string in alist:
    print(string)
    sendmsg(string + ".", chnlId)
    time.sleep(0.2)
