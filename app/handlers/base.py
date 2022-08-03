
from tornado.web import RequestHandler
from tornado.web import authenticated
from urllib.parse import parse_qs

import tornado_swirl as swirl


class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

@swirl.restapi('/')
class MainHandler(BaseHandler):
    @authenticated
    def get(self):
        """
        This is the main handler for the API.
        """
        data = {"msg":"Hello, world"}
        self.write(data)

