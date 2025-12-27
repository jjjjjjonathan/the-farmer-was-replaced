import constants, navigation

def wait_for_all_drones(drone_set):
    while len(drone_set) > 0:
        removed_drones = []
        for drone in drone_set:
            if has_finished(drone):
                removed_drones.append(drone)
        for removed_drone in removed_drones:
            drone_set.remove(removed_drone)

def spawn_drones(callback, direction, world_size = get_world_size()):
    drones = set()
    for _ in range(world_size):
        drone = None
        if num_drones() < world_size:
            drone = spawn_drone(callback)
        if not drone:
            callback()
        else:
            drones.add(drone)
        move(direction)
    wait_for_all_drones(drones)

def validate_ground(ground_type):
    if get_ground_type() != ground_type:
        till()

def till_row():
    for _ in range(get_world_size()):
        if can_harvest():
            harvest()
        validate_ground(Grounds.Soil)
        move(East)

def till_all(world_size):
    spawn_drones(till_row, North, world_size)

def till_checkerboard_row(ground_type):
    for _ in range(constants.WS):
        if is_even_tile(get_pos_x(), get_pos_y()):
            validate_ground(ground_type)
        move(East)

def till_checkerboard(ground_type):
    def task():
        till_checkerboard_row(ground_type)
    spawn_drones(task, North, constants.WS)

def maintain_water_level(water_level = 0.75):
    if get_water() < water_level:
        use_item(Items.Water)
        maintain_water_level(water_level)

def get_substance(maze_size):
    return maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)

entities = [Entities.Cactus, Entities.Carrot, Entities.Grass, Entities.Tree, Entities.Bush, Entities.Pumpkin, Entities.Sunflower]

def clear_field():
    for _ in range(constants.WS):
        while get_entity_type() in entities:
            if can_harvest():
                harvest()
            if get_entity_type() == Entities.Grass:
                break
        move(East)

def clean():
    navigation.go(0,0)
    spawn_drones(clear_field, North, constants.WS)

def is_even_tile(x, y):
    return (x + y) % 2 == 0

def plant_friends(entity, world_size):
    for _ in range(world_size):
        if not is_even_tile(get_pos_x(), get_pos_y()):
            plant(entity)
        move(East)

def use_fertilizer(entity):
    if enough_fertilizer() and not regaining_fertilizer() and entity not in constants.NO_FERT:
        use_item(Items.Fertilizer)

def use_weird_substance(entity):
    if enough_fertilizer() and not regaining_fertilizer() and entity not in constants.NO_FERT:
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

def plant_polyculture_crops(entity, world_size, companion, stop = never_stop):
    while not stop():
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
                        while not can_harvest():
                            use_fertilizer(entity)
                            use_weird_substance(entity)
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

def enough_fertilizer():
    return num_items(Items.Fertilizer) >= constants.MIN_FERTILIZER

def regaining_fertilizer():
    return num_items(Items.Fertilizer) < constants.MAX_FERTILIZER

def stop_polyculture():
    return not enough_fertilizer() or not enough_power()

def start_and_continue_polyculture():
    return enough_power() and not regaining_fertilizer()
