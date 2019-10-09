import os
import sys
import requests
import pathlib
import traceback
import pprint
from html.parser import HTMLParser


URL_BASE = "http://172.20.7.90/redmine"


class Parser(HTMLParser):
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


def analyzeAttachmentToken(js_body):
    index_start = js_body.find("val(") + 4
    index_end = index_start + 69
    attachment_token = js_body[index_start:index_end]
    return attachment_token


def analyzeToken(html_body):
    """HTMLボディを解析して、認証トークンを取得する.
    """
    parser = Parser()
    parser.feed(html_body)
    parser.close()
    return parser.authenticity_token


def transition(session, page_name):
    """ページ遷移して認証トークンを取得する.
    """
    res = session.get(url=URL_BASE+page_name)
    return analyzeToken(res.text)


def login(session):
    print("==== login start. ====")
    USER = "ninomiya"
    PASS = "MakotoNinomiya"
    post = {
        'username': USER,
        'password': PASS,
        'authenticity_token': token
    }
    res = session.post(url=URL_BASE+"/login", data=post)
    # print(res.text)
    pprint.pprint(res.headers)
    res.close()
    print("==== login end. ====")


def attachment(session, page_name, file_name, token):
    print("==== attachment start.")
    url = "http://172.20.7.90/redmine/uploads.js?attachment_id=1&filename=" + \
        file_name + "&content_type=pdf"
    header = {
        "X-CSRF-Token": token,
        "Referer": "http://172.20.7.90/redmine/projects/iij/wiki/Python3",
        "Accept": "application/js",
        "Content-Type": "application/octet-stream"
    }
    post = {
        'authenticity_token': token
    }
    res = session.post(url=url, headers=header, data=post)
    print(res)
    if res.status_code == 200:
        print(res.text)
        return analyzeAttachmentToken(res.text)
    print("==== attachment end.")


def upload(session, file_name, token, attachement_token):
    print("==== upload start.")
    path_base = os.path.dirname(os.path.abspath(__file__))
    path_file = os.path.normpath(os.path.join(path_base, "./" + file_name))
    with pathlib.Path(path_file).open(mode='rb') as f:
        header = {
            "X-CSRF-Token": token,
            "Referer": "http://172.20.7.90/redmine/projects/iij/wiki/Python3"
        }
        post = {
            'attachment[1][filename]': "download.pdf",
            'attachment[1][description]': "test",
            'attachment[1][token]': attachment_token,
            'authenticity_token': token
        }
        fileinfo = {
            'attachment[dummy][file]': (f.read(), "application/octet-stream")
        }
        res = session.post(
            url="http://172.20.7.90/redmine/projects/iij/wiki/Python3/add_attachment", headers=header, data=post, files=fileinfo)
        print(res)
        print(res.text)
    print("==== upload end.")

if __name__ == "__main__":
    try:
        session = requests.session()
        # ログイン画面へ遷移してトークンを取得
        token = transition(session, "/login")
        # ログイン
        login(session)
        # ページ遷移してトークンを取得
        token = transition(session, "/projects/iij/wiki/Python3")
        # アップロード準備
        attachment_token = attachment(session, "/projects/iij/wiki/Python3", "download.pdf", token)
        print("____ attachment_token : " + attachment_token)
        # アップロード
        upload(session, "download.pdf", token, attachment_token)
    except Exception as e:
        except_str = traceback.format_exc()
        print('例外を文字列として表示')
        print(except_str)
        print('表示終了')
