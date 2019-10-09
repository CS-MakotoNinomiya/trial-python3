import os
import sys
import requests
import pathlib
import traceback
import pprint
from html.parser import HTMLParser


class TestParser(HTMLParser):
    authenticity_token = ""
    def handle_starttag(self, tagname, attribute):
        if tagname.lower() == 'input':
            is_token = False
            for i in attribute:
                if i[0].lower() == 'name' and i[1].lower() == "authenticity_token":
                    is_token = True
                if is_token and i[0].lower() == "value":
                    self.authenticity_token = i[1]
                    is_token = False
                    continue


def analyzeToken(html_body):
    parser = TestParser()
    parser.feed(html_body)
    parser.close()
    return parser.authenticity_token


if __name__ == "__main__":
    try:
        session = requests.session()
        # ログイン画面へ遷移
        res = session.get("http://172.20.7.90/redmine/login")
        body = res.text
        res.close()
        # アクセストークンを取得
        token = analyzeToken(body)
        print("____ token : " + token)
    except Exception as e:
        except_str = traceback.format_exc()
        print('例外を文字列として表示')
        print(except_str)
        print('表示終了')
