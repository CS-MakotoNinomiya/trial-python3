import os
import datetime
import pathlib

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, "./conf/sample.txt"))

print(pathlib.Path(name).exists())

try:
    dt_now = datetime.datetime.now()
    file = open(name, 'a')
    file.write("{0:%Y-%m-%d %H:%M:%S}".format(dt_now) + " write to file.\n")
except Exception as e:
    print(e)
finally:
    file.close()
