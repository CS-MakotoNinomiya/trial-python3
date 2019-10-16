import os
import sys
import logging.config
import pathlib

def getFilePath(relative_path):
    path_base = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(path_base, relative_path))

logging.config.fileConfig(getFilePath("./conf/logging.conf"))
logger = logging.getLogger()

if __name__ == "__main__":
    logger.debug("test.")
