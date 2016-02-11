import numpy as np

def initMap(row, col):
    sim_area = np.zeros((row,col))
    sim_area = sim_area.astype('O')
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

if __name__ == '__main__':
    area = initMap(20, 20)
    area[1,1] = [1,2,3]
    area[0,0] = {"id": "xyzdw"}
    print(area)