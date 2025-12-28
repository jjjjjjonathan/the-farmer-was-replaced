import navigation, farm_utils
from constants import WS

ws = WS

def polyculture_farm_grass():
    while farm_utils.enough_power():
        farm_utils.plant_polyculture_crops(Entities.Grass, ws, Entities.Bush, True)

def need_friends():
    farm_utils.plant_friends(Entities.Bush, ws)

def farm():
    while farm_utils.enough_power():
        navigation.go(0,0)
        # change even tiles to grassland so grass regrows itself after harvest
        if get_ground_type() != Grounds.Grassland:
            farm_utils.till_checkerboard(Grounds.Grassland)
        farm_utils.spawn_drones(need_friends, North, ws)
        farm_utils.spawn_drones(polyculture_farm_grass, North, ws)
