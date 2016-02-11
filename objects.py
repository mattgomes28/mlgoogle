# This is the class file
# all classes go here.
import math

class Drone(object):
	limit = 0
	location = []
	dest = []
	items = []
	tasks = []
	units = 0

	def __init__(self, l, loc, dest):
		self.limit = l
		self.location = loc
		self.dest = dest
		self.fly(dest)


	def load(self, warehouse, items):
		# bit or error checking
		assert limit >= sum(list(map((lambda x: x.get_weight), items)))
		tasks.append(("l", (warehouse, items)))

	def fly(self, l):
		self.dest = l
		self.units = math.sqrt((location[0] - l[0])**2 + (location[1] - l[1])**2)

	def deliver(self, t_items): #t_items[i] = (item, location)
		for (item, location) in t_items: self.task.append(("d", item, location))


	def update(self):
		if self.units > 0 : self.units -= self.units
		else: 
			if self.tasks[0][0] == "l": 
				self.tasks[0][1].load(self.tasks[0][2])
			self.location = self.dest
			if self.tasks != []: 
				del(self.tasks[0])
				if self.tasks != [] and self.tasks[0][0] == "d": 
					self.dest = tassk[0][1]
					self.fly(self.dest)
				elif self.tasks != [] and self.tasks[0][0] == "l":
					self.dest = self.tasks[0][0].location
					self.fly(self.dest)

class Warehouse(object):

    def __init__(self, loc, items):
        self.location = loc
        self.items = items # List containing quantity of each item available in warehouse

    def get_stock(self, product_type):
        # The number of items product_type available in the warehouse
        return self.items[product_type]

    def load(self, items):
        for item_type in items:
            self.items[item_type] -= 1

    def unload(self, items):
        for item_type in items:
            self.items[item_type] += 1

    def is_in_stock(self, product_type):
        return True if self.items[product_type]>0 else False

class Order(object):

    def __init__(self, loc, items):
        self.location = loc # order location
        self.items = items # items of type x ordered in a list

class Cell(object):

    def __init__(self):
        self.drones = []
        self.warehouse = None
        self.order = None
