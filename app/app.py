#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import asyncio
import tornado.httpserver
import tornado.options
import tornado.web
import tornado_swirl as swirl
import os

from config import urls
from tornado.options import define, options
from config.settings import settings

define("port", default=8000, help="run on the given port", type=int)

async def main():
    tornado.options.parse_command_line()
    base_dir = os.path.dirname(__file__)
    env_settings = {
            'cookie_secret' : settings.cookie_secret,
            'login_url' : '/login',
            'template_path' : os.path.join(base_dir, 'templates'),
            'static_path' : os.path.join(base_dir, 'static'),
            'debug' : True,
            'xsrf_cookies' : False,
        }
    application = swirl.Application(
        swirl.api_routes(), 
        **env_settings)
    print('*Urls')
    for route in swirl.api_routes(): print(route)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
