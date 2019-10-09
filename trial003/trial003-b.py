import os
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
    # pprint.pprint(res.getheaders())
    # pprint.pprint(res.read().decode("utf-8"))
    res.close()


def downloadCsv(opener, file_name):
    with opener.open("http://172.20.7.90/redmine/projects/iij/issues.csv") as res:
        csvData = res.read().decode("MS932")
        # csv出力
        path_base = os.path.dirname(os.path.abspath(__file__))
        path_file = os.path.normpath(os.path.join(path_base, "./" + file_name))
        with pathlib.Path(path_file).open(mode='w') as f:
            f.write(csvData)
            res.close()


def downloadPdf(opener, file_name):
    with opener.open("http://172.20.7.90/redmine/projects/iij/issues.pdf") as res:
        path_base = os.path.dirname(os.path.abspath(__file__))
        path_file = os.path.normpath(os.path.join(path_base, "./" + file_name))
        with pathlib.Path(path_file).open(mode='wb') as f:
            while 1:
                packet = res.read()
                if not packet:
                    break
                f.write(packet)


if __name__ == "__main__":
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    # アクセストークンを取得
    token = analyzeToken(opener)
    print(token)
    # ログイン
    login(opener)
    # csvダウンロード
    downloadCsv(opener, "download.csv")
    # padダウンロード
    downloadPdf(opener, "download.pdf")
