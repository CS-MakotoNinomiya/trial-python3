import os
import sys
import traceback
import pathlib
import pprint
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from urllib.request import urlretrieve
from http.cookiejar import CookieJar

def analyzeToken(opener):
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

    return token


def login(opener):
    USER = "ninomiya"
    PASS = "MakotoNinomiya"
    post = {
        'username': USER,
        'password': PASS,
        'authenticity_token': token
    }
    data = urlencode(post).encode("utf-8")
    res = opener.open("http://172.20.7.90/redmine/login", data)
    res.close()


def upload(opener, file_name):
    path_base = os.path.dirname(os.path.abspath(__file__))
    path_file = os.path.normpath(os.path.join(path_base, "./" + file_name))
    with pathlib.Path(path_file).open(mode='rb') as f:
        post = {
            "authenticity_token": token,
            "attachments[1][filename]": "hogehoge.png",
            "attachments[1][description]": "",
            "attachments[dummy][file]": f.read()
        }
        data = urlencode(post).encode()
        opener.open(
            "http://172.20.7.90/redmine/projects/iij/wiki/ファイルダウンロード/add_attachment", data)


if __name__ == "__main__":
    try:
        opener = build_opener(HTTPCookieProcessor(CookieJar()))
        # アクセストークンを取得
        token = analyzeToken(opener)
        print(token)
        # ログイン
        login(opener)
        # アップロード
        upload(opener, "download.pdf")
    except Exception as e:
        except_str = traceback.format_exc()
        print('例外を文字列として表示')
        print(except_str)
        print('表示終了')
