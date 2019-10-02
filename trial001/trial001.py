import os
import pathlib

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, "./conf/sample.txt"))

print(pathlib.Path(name).exists())
