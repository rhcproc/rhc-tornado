
from handlers.base import BaseHandler
from handlers.utils import now2str

import tornado_swirl as swirl
import json

@swirl.restapi('/api/v1/dashboard')
class DashboardHandler(BaseHandler):
    def get(self):
        data = {'result':now2str()}
        self.write(data)
