# -*- coding: utf-8 -*-
# CREATED: 2023/7/5
# AUTHOR : NOAH YOUNG
# EMAIL  : noah227@foxmail.com

import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse

from src.core import IpFetcher

HOST_LIST_PATH = os.path.join(os.path.dirname(__file__), "../domain-list.txt")


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/favicon"):
            return self.response({}, False)
        queryRaw = parse.urlparse(self.path).query
        query = parse.parse_qs(queryRaw)
        urls = query.get("urls")
        requestPlain = query.get("plain")
        urlList = []
        if urls and len(urls):
            urlList = urls[0].split(",")
        elif os.path.exists(HOST_LIST_PATH):
            urlList = []
            # 加载默认配置
            with open(HOST_LIST_PATH, "r", encoding="utf8") as f:
                while _ := f.readline():
                    _ = _.strip()
                    _ and not _.startswith("#") and urlList.append(_.strip())
        data = IpFetcher(urlList).run().result
        self.response(data, requestPlain)

    def response(self, data, plain):
        self.send_response(200)
        if plain:
            self.send_header("ContentType", "text/plain")
            [_.reverse() for _ in data]
            resData = "\n".join([" ".join(_) for _ in data])
        else:
            self.send_header("ContentType", "application/json")
            resData = json.dumps(data)
        self.end_headers()
        self.wfile.write(resData.encode(encoding="utf8"))
        pass


class Server:
    def __init__(self, host, port=80):
        self.host = host
        self.port = port
        self.server = HTTPServer((self.host, self.port), HttpHandler)
        pass

    def run(self):
        print(f"Server started at http://{self.host}:{self.port}")
        self.server.serve_forever()
        pass


if __name__ == '__main__':
    Server("0.0.0.0", 9999).run()
    pass
