import constants, navigation, drone_utils

def validate_ground(ground_type):
    if get_ground_type() != ground_type:
        till()

def till_row():
    for _ in range(constants.WS):
        if can_harvest():
            harvest()
        validate_ground(Grounds.Soil)
        move(East)

def till_all():
    drone_utils.spawn_drones(till_row, North)

def till_checkerboard_row(ground_type):
    for _ in range(constants.WS):
        if is_even_tile(get_pos_x(), get_pos_y()):
            validate_ground(ground_type)
        move(East)

def till_checkerboard(ground_type):
    def task():
        till_checkerboard_row(ground_type)
    drone_utils.spawn_drones(task, North)

def maintain_water_level(water_level = 0.75):
    if get_water() < water_level:
        use_item(Items.Water)
        maintain_water_level(water_level)

def get_substance(maze_size):
    return maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)

def clear_field():
    for _ in range(constants.WS):
        while get_entity_type() in constants.ENTITIES:
            if can_harvest():
                harvest()
            if get_entity_type() == Entities.Grass:
                break
        move(East)

def clean():
    navigation.go(0,0)
    drone_utils.spawn_drones(clear_field, North)

def is_even_tile(x, y):
    return (x + y) % 2 == 0

def plant_friends(entity, world_size = constants.WS):
    for _ in range(world_size):
        if not is_even_tile(get_pos_x(), get_pos_y()):
            plant(entity)
        move(East)

def use_fertilizer(entity, is_recharging):
    if not is_recharging and entity not in constants.NO_FERT:
        use_item(Items.Fertilizer)

def use_weird_substance(entity, is_recharging):
    if not is_recharging and entity not in constants.NO_FERT:
        use_item(Items.Weird_Substance)
	
def never_stop():
    return False

def match_entity_to_item(entity):
    if entity == Entities.Grass:
        return Items.Hay
    if entity == Entities.Tree or entity == Entities.Bush:
        return Items.Wood
    if entity == Entities.Carrot:
        return Items.Carrot

def plant_polyculture_crops(entity, companion, is_recharging, world_size = constants.WS):
    for _ in range(world_size):
        if is_even_tile(get_pos_x(), get_pos_y()):
            waiting_for_poly_crop = True
            while waiting_for_poly_crop:
                if get_entity_type() != entity:
                    if entity != Entities.Grass:
                        plant(entity)
                    maintain_water_level()
                plant_friend, (fx, fy) = get_companion()
                
                if plant_friend == companion and not is_even_tile(fx, fy):
                    if not can_harvest():
                        use_fertilizer(entity, is_recharging)
                        use_weird_substance(entity, is_recharging)
                    while not can_harvest():
                        pass
                    harvest()
                    if entity != Entities.Grass:
                        plant(entity)
                    maintain_water_level()
                    waiting_for_poly_crop = False
                else:
                    harvest()
        move(East)

def random_index(list_length):
    return random() * list_length // 1

def enough_power():
    return num_items(Items.Power) >= constants.MIN_POWER

def farm_polyculture_row(entity, companion, stop = never_stop):
    while not stop():
        while not stop_polyculture():
            plant_polyculture_crops(entity, companion, False)        
        if not enough_power():
            break
        while regaining_fertilizer() and enough_power():
            plant_polyculture_crops(entity, companion, True)

def farm_polyculture_row_no_fert(entity, companion, stop = never_stop):
    while not stop():
        plant_polyculture_crops(entity, companion, True)

def enough_fertilizer():
    return num_items(Items.Fertilizer) >= constants.MIN_FERTILIZER

def regaining_fertilizer():
    return num_items(Items.Fertilizer) < constants.MAX_FERTILIZER

def stop_polyculture():
    return not enough_fertilizer() or not enough_power()

def start_and_continue_polyculture():
    return enough_power() and not regaining_fertilizer()
