# 02/11/2014 13:40
# UA Kiryaziev

import tornado.httpserver
import tornado.ioloop
import tornado.web

from mysql_data import MySQLData

from index_handler import IndexHandler
from phones_handler import PhonesHandler
from insert_handler import InsertHandler
from ws_handler import WSHandler


def main():
    #conn_pool = MySQLData.connect_to_db("192.168.1.250", "admin", "admin", "testdb")

    application = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/phones", PhonesHandler),
        #(r"/insert", InsertHandler, {"conn_pool": conn_pool}),
        (r"/ws", WSHandler),
    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8008, "192.168.1.2")
    #http_server.bind(8008, "192.168.1.250")
    #http_server.start(0)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    print("Started at 192.168.1.250:8008")
    main()