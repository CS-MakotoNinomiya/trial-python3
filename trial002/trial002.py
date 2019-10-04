import os
import datetime
import pathlib

# 相対パスでファイルパス
path_base = os.path.dirname(os.path.abspath(__file__))
path_file = os.path.normpath(os.path.join(path_base, "./tmp/sample.txt"))


def datetime_now():
    return datetime.datetime.now()


with pathlib.Path(path_file).open(mode='a') as f:
    print("ファイルに書き出し")
    # 追記モードでファイルオープン
    f.write("{0:%Y-%m-%d %H:%M:%S}".format(datetime_now()) + " start.\n")
    f.write("{0:%Y-%m-%d %H:%M:%S}".format(datetime_now()) + " end.\n\n")
    f.flush()

with pathlib.Path(path_file).open(mode='r') as f:
    print("ファイル読み込み（全行版）")
    # 全行読み込み（行数が少ないことが分かっている場合）
    lines = f.readlines()
    for line in lines:
        line = line.strip()    # remove line separator
        print(line)

with pathlib.Path(path_file).open(mode='r') as f:
    print("ファイル読み込み（１行ずつ版）")
    # 1行ずつ読み込み（行数が多い、多くなることが分かっている場合）
    line = f.readline()
    while line:
        line = line.strip()    # remove line separator
        print(line)
        line = f.readline()
