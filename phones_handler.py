# 03/11/2014 17:15
# UA Kiryaziev

import tornado.web

from mysql_data import MySQLData


class PhonesHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write('Hello Phones!')
        self.finish()

    @tornado.web.asynchronous
    def post(self):
        phone = self.get_body_argument("phone", default=0)

        md = MySQLData()
        md.connect_to_db("192.168.1.250", "admin", "admin", "phones_nv")
        result = md.get_data_by_phone(phone)
        md.disconnect_from_db()

        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(result)
        self.finish()