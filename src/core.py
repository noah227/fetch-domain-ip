# -*- coding: utf-8 -*-
# CREATED: 2023/7/5
# AUTHOR : NOAH YOUNG
# EMAIL  : noah227@foxmail.com

import socket
import threading
from concurrent.futures import ThreadPoolExecutor


class IpFetcher:
    def __init__(self, urlList):
        self.urlList = urlList
        self.result = []
        pass

    def getSiteIp(self, url):
        if not url:
            return
        try:
            info = socket.getaddrinfo(url, 80, 0, 0, socket.SOL_TCP)
            with threading.Lock():
                self.result.append([url, info[0][4][0]])
        except Exception as e:
            print(e)
        pass

    def run(self, verbose=False):
        with ThreadPoolExecutor() as executor:
            executor.map(self.getSiteIp, (i.strip() for i in self.urlList))
            pass
        verbose and self.verboseLog()
        return self

    def verboseLog(self):
        for url, ip in self.result:
            print(f"{ip} {url}")
        pass


if __name__ == '__main__':
    _urlList = []
    # 加载默认配置
    with open("../domain-list.txt", "r", encoding="utf8") as f:
        while _ := f.readline():
            not _.startswith("#") and _urlList.append(_.strip())
    IpFetcher(_urlList).run(True)
    pass
