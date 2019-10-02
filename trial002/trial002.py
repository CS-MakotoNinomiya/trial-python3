import os
import pathlib

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, "./conf/sample.txt"))

file_path = pathlib.Path(name)

if file_path.exists():

    with file_path.open(mode='r') as f:
        line = f.readline()
        while line:
            line = line.rstrip('\r\n').rstrip('\n')    # remove line separator
            print(line)
            line = f.readline()
        f.close()

    with file_path.open(mode='r') as f:
        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.rstrip('\r\n').rstrip('\n')    # remove line separator
            print(line)
