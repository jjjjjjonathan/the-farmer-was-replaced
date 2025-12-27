import navigation, farm_utils, constants

ws = constants.WS

def tree_lines():
    for _ in range(ws):
        if can_harvest():
            harvest()
        if farm_utils.is_even_tile(get_pos_x(), get_pos_y()):
            plant(Entities.Tree)
        else:
            plant(Entities.Bush)
        farm_utils.maintain_water_level()
        move(East)

def farm_regular_wood():
    while farm_utils.regaining_fertilizer() and farm_utils.enough_power():
        tree_lines()

def polyculture_farm_wood():
    farm_utils.plant_friends(Entities.Grass, ws)
    farm_utils.plant_polyculture_crops(Entities.Tree, ws, Entities.Grass, farm_utils.stop_polyculture)

def farm():
    if farm_utils.start_and_continue_polyculture():
        navigation.go(0,0)
        farm_utils.spawn_drones(polyculture_farm_wood, North, ws)
    navigation.go(0,0)
    farm_utils.spawn_drones(farm_regular_wood, North, ws)
