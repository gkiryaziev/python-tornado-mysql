# 02/11/2014 13:40
# UA Kiryaziev

import tornado.httpserver
import tornado.ioloop
import tornado.web

from index_handler import IndexHandler
from phones_handler import PhonesHandler


def main():
    application = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/phones", PhonesHandler),
    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8008, address="192.168.1.2")
    # http_server.bind(8008, address="192.168.1.2")
    # http_server.start(0)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    print("Started at 192.168.1.250:8008")
    main()