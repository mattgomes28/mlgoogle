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

class Warehouse(object):

    def __init__(self, loc, items):
        self.location = loc
        self.items = items # List containing quantity of each item available in warehouse

    def get_stock(self, product_type):
        # The number of items product_type available in the warehouse
        return items[product_type]

    def load(self, items):
        for item_type in items:
            self.items[item_type] -= 1

    def unload(self, items):
        for item_type in items:
            self.items[item_type] += 1

    def is_in_stock(self, product_type):
        return True if items[product_type]>0 else False

class Order(object):

    def __init__(self, loc, items):
        self.location = loc # order location
        self.items = items # items of type x ordered in a list

