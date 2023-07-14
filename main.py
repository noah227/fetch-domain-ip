import os
from configparser import ConfigParser

from src.server import Server

CONFIG_PATH = "./server.ini"


def runServer():
    host = "127.0.0.1"
    port = 9999
    # 读取配置文件
    if os.path.exists(CONFIG_PATH):
        cp = ConfigParser()
        cp.read(CONFIG_PATH, encoding="utf8")
        cHttp = cp["http"]
        host = cHttp["host"]
        port = int(cHttp["port"])
    Server(host, port).run()
    pass


if __name__ == '__main__':
    runServer()
