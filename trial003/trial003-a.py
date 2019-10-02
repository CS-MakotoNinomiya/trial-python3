import urllib.request

req = urllib.request.Request("http://172.20.7.90/redmine/issues/109")
with urllib.request.urlopen(req) as res:
    body = res.read()
    print(body)