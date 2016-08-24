# coding:utf8

import os.path
import sys
import socket

sys.path.append('/usr/local/lib/python2.7/site-packages/')


import torndb
import tornado.options
from tornado import httpserver, ioloop, web
from tornado.options import define, options
from handlers import HANDLERS, TEMPLATE_PATH


define('port', default = 9000, help = 'run on the given port', type = int)
define('mysql_host', default='127.0.0.1:3306', help = 'blog database host')
define('mysql_database', default='test', help= 'blog database name')
define('mysql_user', default='root', help='blog database user')
define('mysql_password', default='root', help='blog database password')

 
class Application(web.Application):
	def __init__(self):
		handlers = HANDLERS
		settings = dict(
			template_path = TEMPLATE_PATH,
			xsrf_cookies = False,
			cookie_secret = 'rihqgy5wTiGI8X0+yQ9k6lRo0iYIm0folFapDESYkJ4='
			)

		web.Application.__init__(self, handlers, **settings)

		self.db = torndb.Connection(
			host = options.mysql_host,
			database = options.mysql_database,
			user = options.mysql_user,
			password = options.mysql_password
			)



if __name__ == '__main__':
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()


	