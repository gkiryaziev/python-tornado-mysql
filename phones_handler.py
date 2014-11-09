# 03/11/2014 17:15
# UA Kiryaziev

import tornado.web

from mysql_data import MySQLData


class PhonesHandler(tornado.web.RequestHandler):
    def initialize(self, conn):
        self.conn = conn

    @tornado.web.asynchronous
    def get(self):
        self.write('Hello Phones!')
        self.finish()

    @tornado.web.asynchronous
    def post(self):
        phone = self.get_body_argument("phone", default=0)

        db_result = MySQLData.get_data_by_phone(self.conn, phone)

        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(db_result)
        self.finish()