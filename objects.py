# This is the class file
# all classes go here.


class Drone(object):
	limit = 0
	location = []

	def __init__(self, l, loc):
		self.limit = l
		self.location = loc

	def load(self, warehouse, items):
		self.fly(warehouse)
