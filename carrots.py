import navigation, farm_utils, constants

ws = constants.WS

def not_enough_power():
    return not farm_utils.enough_power()

def polyculture_farm_carrots():
    farm_utils.plant_friends(Entities.Grass, ws)
    farm_utils.plant_polyculture_crops(Entities.Carrot, ws, Entities.Grass, not_enough_power)

def farm():
     # polyculture farming
    if farm_utils.enough_power():
        navigation.go(0,0)
        if get_ground_type() != Grounds.Soil:
            farm_utils.till_checkerboard(Grounds.Soil)
        farm_utils.spawn_drones(polyculture_farm_carrots, North, ws)

