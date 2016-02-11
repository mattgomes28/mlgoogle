import numpy as np

def initMap(row, col):
    sim_area = np.zeros((row,col))
    return sim_area

def populateMap(area, pos, obj):
    """w for warehouse, d for drone, c for customer
    w -> 1, d -> 2, c -> 3"""
    row, col = pos
    if obj == "w":
        area[row,col] = 1
    elif obj == "d":
        area[row,col] = 2
    else:
        area[row,col] = 3

class Warehouse:
    def __init__(self, _id, pos, items):
        self.pos = pos
        self.items = items
        self._id = _id

if __name__ == '__main__':
    area = initMap(20, 20)
    populateMap(area, (3,3), "w")
    populateMap(area, (1,2), "d")
    print(area)