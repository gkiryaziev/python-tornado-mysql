# 03/11/2014 17:15
# UA Kiryaziev

import tornado.web

from mysql_data import MySQLData


class PhonesHandler(tornado.web.RequestHandler):
    def initialize(self, mysql_object):
        self.mysql_object = mysql_object

    def get(self):
        db_result = self.mysql_object.get_data_by_query("all", 0)
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(db_result)

    def post(self):
        phone = self.get_body_argument("phone", default=0)
        db_result = self.mysql_object.get_data_by_query("phone", phone)
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.write(db_result)