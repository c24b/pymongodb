from pymongo import MongoClient
from pymongo import errors
import re
class Model(object):
	def __init__(self):
		self.value1 = "value1"
		self._private = "private value"
		self.value2 = "value2"
class Database(object):
	'''Database creation''' 
	def __init__(self, database_name):
		self.name = database_name
		client = MongoClient('mongodb://localhost,localhost:27017')
		self.db = client[self.name]

	def create_documents(self, object):
		for k in object.__dict__:
			if k[0] != "_":
				 print object.__dict__[k]



if __name__ == '__main__':
	m = Model()
	d = Database('test_ODM')
	d.create_documents(m)