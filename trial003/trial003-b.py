from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import pprint

opener = build_opener(HTTPCookieProcessor(CookieJar()))

res = opener.open("http://172.20.7.90/redmine/login")
body = res.read().decode("utf-8")
res.close()

index_start = body.find("name=\"authenticity_token\"") + 25
index_end = index_start + 100
tmp = body[index_start:index_end]

index_start = tmp.find("value=\"") + 7
index_end = index_start + 100
tmp = tmp[index_start:index_end]

index_start = 0
index_end = tmp.find("\" />")
token = tmp[index_start:index_end]

print(token)

USER = "ninomiya"
PASS = "MakotoNinomiya"

post = {
        'username':USER,
        'password':PASS,
        'authenticity_token':token
        }
data = urlencode(post).encode("utf-8")

res = opener.open("http://172.20.7.90/redmine/login", data)

pprint.pprint(res.getheaders())
pprint.pprint(res.read().decode("utf-8"))

res.close()
