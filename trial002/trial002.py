import os
import sys
import datetime
import pathlib
import traceback

# 相対パスでファイルパス
path_base = os.path.dirname(os.path.abspath(__file__))
path_file = os.path.normpath(os.path.join(path_base, "./tmppp/sample.txt"))


def datetime_now():
    """ 現在日時を取得する.
    \n説明文１
    \n説明文２
    """
    return datetime.datetime.now()


try:
    with pathlib.Path(path_file).open(mode='a') as f:
        print("ファイルに書き出し")
        # 追記モードでファイルオープン
        f.write("{0:%Y-%m-%d %H:%M:%S}".format(datetime_now()) + " start.\n")
        f.write("{0:%Y-%m-%d %H:%M:%S}".format(datetime_now()) + " end.\n\n")
        f.flush()
except Exception as e:
    print("Unexpected error:", e)
    except_str = traceback.format_exc()
    print('==== exception traceback start.')
    print(except_str)
    print('==== exception traceback end.')

try:
    with pathlib.Path(path_file).open(mode='r') as f:
        print("ファイル読み込み（全行版）")
        # 全行読み込み（行数が少ないことが分かっている場合）
        lines = f.readlines()
        line_array = []
        for line in lines:
            line = line.strip()    # remove line separator
            line_array.append(line)
            print(line)
        print("2019-10-04 10:13:36 start." in line_array)
except Exception as e:
    except_str = traceback.format_exc()
    print('==== exception traceback start.')
    print(except_str)
    print('==== exception traceback end.')

try:
    with pathlib.Path(path_file).open(mode='r') as f:
        print("ファイル読み込み（１行ずつ版）")
        # 1行ずつ読み込み（行数が多い、多くなることが分かっている場合）
        line = f.readline()
        while line:
            line = line.strip()    # remove line separator
            if "2019-10-04 10:13:36 start." == line:
                print("True")
            print(line)
            line = f.readline()
except Exception as e:
    except_str = traceback.format_exc()
    print('==== exception traceback start.')
    print(except_str)
    print('==== exception traceback end.')
