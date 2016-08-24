# coding:utf8

import tornado.web
import tornado.gen

class BaseHandler(tornado.web.RequestHandler):
	@property 
	def db(self):
		return self.application.db

	def get_one_poem(self, ids):
		return self.db.get('select * from authors where id=%s', int(ids))

	def get_all(self):
		return self.db.query('select * from authors')

class IndexHandler(BaseHandler):
	def get(self):
		self.render('index.html')


class PoemPageHandler(BaseHandler):
	def post(self):
		noun1 = self.get_argument('noun1')
		noun2 = self.get_argument('noun2')
		verb = self.get_argument('verb')
		noun3 = self.get_argument('noun3')
		self.db.execute('insert into authors (email, name) values(%s,%s)', noun1, noun2)
		ret = self.db.get('select * from authors where email = %s', noun1)
		self.render('poem.html', roads = noun1, wood = noun2, made = verb, difference = noun3, id=ret['id'])


class ShowHandler(BaseHandler):
	def get(self):
		ids = self.get_argument('id', 1)
		ret = self.get_one_poem(ids)
		if not ret:
			raise tornado.web.HTTPError(404)
		self.render('show.html', title = ret['email'], update = ret['name'])

