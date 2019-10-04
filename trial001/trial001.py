import os
import datetime
import pathlib

# 相対パスでファイルアクセス
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.normpath(os.path.join(base_path, "./conf/sample.txt"))
# ファイルの存在確認
print(pathlib.Path(file_path).exists())

try:
    dt_now = datetime.datetime.now()
    # 追記モードでファイルオープン
    file = open(file_path, 'a')
    file.write("{0:%Y-%m-%d %H:%M:%S}".format(dt_now) + " write to file.\n")
except Exception as e:
    print(e)
finally:
    file.close()
