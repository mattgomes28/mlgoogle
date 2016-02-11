# This is the main file
# for the challenge. Please
# post all your code here.

def get_data(file_name):
	f = open(file_name, "r")
	LIST_WAREHOUSES = [] # list of warehouses (tuples)
	LIST_ORDER = [] # list of warehouses (tuples)

	#Default configs - mapping the file to ints
	(ROWS, COLS, DRONES, TURNS, W_LIMIT) = list(map(int, f.readline().split(" ")))
	N_TYPES = int(f.readline()) # N of products
	P_WEIGHTS = list(map(int, f.readline().split(" ")))


	N_WAREHOUSES = int(f.readline())
	# After getting n of warehouses 
	for i in range(0, N_WAREHOUSES):
		loc = list(map(int, f.readline().split(" "))) # should be an array of size 2 (r, c)
		items = list(map(int, f.readline().split(" "))) # items
		warehouse = (loc, items)
		LIST_WAREHOUSES.append(warehouse) # append warehouse to list

	N_ORDERS = int(f.readline())
	# After getting n of orders
	for i in range(0, N_ORDERS):
		loc = list(map(int, f.readline().split(" "))) # should be an array of size 2 (r, c)
		number = int(f.readline()) #number of items
		items = list(map(int, f.readline().split(" "))) # The items in the order
		order = (loc, number, items)
		LIST_ORDER.append(order)

	return (ROWS, COLS, DRONES, TURNS, W_LIMIT, LIST_WAREHOUSES, LIST_ORDER)






if __name__ == "__main__":
	(ROWS, COLS, DRONES, TURNS, W_LIMIT, LIST_WAREHOUSES, LIST_ORDER) = get_data("mother_of_all_warehouses.in")
	print("Rows: " + str(ROWS))
	print("Cols: " + str(COLS))
	print("Drones: " + str(DRONES))
	print("Weight limit: " + str(W_LIMIT))
	print("N of warehouses: " + str(len(LIST_WAREHOUSES)))
	print("N of orders: " + str(len(LIST_ORDER)))