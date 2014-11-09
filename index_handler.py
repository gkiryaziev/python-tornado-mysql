# 09/11/2014 18:16
# UA Kiryaziev

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write('Hello Index!')
        self.finish()