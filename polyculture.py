import navigation, farm_utils

clear()
ws = get_world_size()
farm_utils.till_all(ws)

def wait_to_harvest():
    if get_entity_type() != None:
        use_item(Items.Fertilizer)
        while not can_harvest():
            pass
        use_item(Items.Weird_Substance)
        harvest()

def plant_next(next_coord, next_plant):
    x,y = next_coord
    navigation.go(x,y)
    wait_to_harvest()
    plant(next_plant)
    farm_utils.maintain_water_level()

def harvest_prev(prev_coord, next_coord):
    x_prev, y_prev = prev_coord
    navigation.go(x_prev,y_prev)
    wait_to_harvest()
    x_next, y_next = next_coord
    navigation.go(x_next, y_next)

def polyculture_farm():
    plant(Entities.Tree)
    farm_utils.maintain_water_level()
    use_item(Items.Fertilizer)
    companion = get_companion()
    while companion != None:
        prev_coord = (get_pos_x(), get_pos_y())
        next_plant, next_coord = companion
        plant_next(next_coord, next_plant)
        harvest_prev(prev_coord, next_coord)
        companion = get_companion()

def clean():
    farm_utils.clean(ws)

while True:
    navigation.go(0,0)
    farm_utils.spawn_drones(polyculture_farm, North, ws)
    navigation.go(0,0)
    farm_utils.spawn_drones(clean, North, ws)
