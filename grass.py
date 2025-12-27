import navigation, farm_utils
from constants import WS

ws = WS

def stop_grass_polyculture():
    return not farm_utils.enough_power()

def polyculture_farm_grass():
    farm_utils.plant_friends(Entities.Bush, ws)
    farm_utils.plant_polyculture_crops(Entities.Grass, ws, Entities.Bush, stop_grass_polyculture)

def farm():
    while farm_utils.enough_power():
        navigation.go(0,0)
        # change even tiles to grassland so grass regrows itself after harvest
        if get_ground_type() != Grounds.Grassland:
            farm_utils.till_checkerboard(Grounds.Grassland)
        farm_utils.spawn_drones(polyculture_farm_grass, North, ws)
