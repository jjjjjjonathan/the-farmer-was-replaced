import navigation, farm_utils, constants

ws = constants.WS

def not_enough_power():
    return not farm_utils.enough_power()

def need_friends():
    farm_utils.plant_friends(Entities.Grass, ws)

def polyculture_farm_carrots():
    farm_utils.farm_polyculture_row(Entities.Carrot, ws, Entities.Grass, not_enough_power)

def farm():
     # polyculture farming
    if farm_utils.enough_power():
        navigation.go(0,0)
        if get_ground_type() != Grounds.Soil:
            farm_utils.till_checkerboard(Grounds.Soil)
        navigation.go(0,1)
        if get_entity_type() != Entities.Grass:
            navigation.go(0,0)
            farm_utils.spawn_drones(need_friends, North, ws)
        navigation.go(0,0)
        farm_utils.spawn_drones(polyculture_farm_carrots, North, ws)

