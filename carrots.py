import navigation, farm_utils, constants

ws = constants.WS

def farm_regular_carrots():
    while farm_utils.regaining_fertilizer() and farm_utils.enough_power():
        for _ in range(ws):
            if can_harvest():
                harvest()
            plant(Entities.Carrot)
            farm_utils.maintain_water_level()
            move(East)

def polyculture_farm_carrots():
    farm_utils.plant_friends(Entities.Grass, ws)
    farm_utils.plant_polyculture_crops(Entities.Carrot, ws, Entities.Grass, farm_utils.stop_polyculture)

def farm():
     # polyculture farming
    if farm_utils.start_and_continue_polyculture():
        navigation.go(0,0)
        if get_ground_type() != Grounds.Soil:
            farm_utils.till_checkerboard(Grounds.Soil)
        farm_utils.spawn_drones(polyculture_farm_carrots, North, ws)

    # regular farming
    navigation.go(0,1)
    if get_ground_type() != Grounds.Soil:
        navigation.go(0,0)
        farm_utils.till_all(ws)
    else:
        navigation.go(0,0)
    farm_utils.spawn_drones(farm_regular_carrots, North, ws)

