# 02/11/2014 20:51
# UA Kiryaziev

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write('Hello World!')
        self.finish()