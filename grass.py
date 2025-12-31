import navigation, farm_utils, drone_utils
from constants import WS

ws = WS

def not_enough_power():
    return not farm_utils.enough_power()

def polyculture_farm_grass():
    while farm_utils.enough_power():
        farm_utils.farm_polyculture_row_no_fert(Entities.Grass, Entities.Bush, not_enough_power)

def need_friends():
    farm_utils.plant_friends(Entities.Bush, ws)

def farm():
    while farm_utils.enough_power():
        navigation.go(0,0)
        # change even tiles to grassland so grass regrows itself after harvest
        if get_ground_type() != Grounds.Grassland:
            farm_utils.till_checkerboard(Grounds.Grassland)
        drone_utils.spawn_drones(need_friends, North)
        drone_utils.spawn_drones(polyculture_farm_grass, North)
