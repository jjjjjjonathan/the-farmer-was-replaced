import navigation, farm_utils

clear()
change_hat(Hats.Golden_Pumpkin_Hat)
ws = get_world_size()
farm_utils.till_all(ws)

def plant_initial_pumpkin_row():
    row = list()
    for _ in range(ws):
        farm_utils.maintain_water_level()
        plant(Entities.Pumpkin)
        row.append((get_pos_x(), get_pos_y()))
        move(East)
    return row

def replace_dead_pumpkins(row):
    while len(row) > 0:
        for (x,y) in row:
            navigation.go(x,y)
            if get_entity_type() == Entities.Dead_Pumpkin:
                plant(Entities.Pumpkin)
            elif can_harvest():
                row.remove((x,y))


def plant_perfect_pumpkin_row():
    change_hat(Hats.Golden_Pumpkin_Hat)
    y = get_pos_y()
    while True:
        row = plant_initial_pumpkin_row()
        replace_dead_pumpkins(row)
        navigation.go(0, y)
        while get_entity_type() == Entities.Pumpkin:
            pass
        if num_items(Items.Pumpkin) > 1000000000 or num_items(Items.Carrot) < 1000000:
            break
		

while True:
    navigation.go(0,0)
    for _ in range(ws):
        spawn_drone(plant_perfect_pumpkin_row)
        move(North)
    while True:
        navigation.go(0, ws - 1)
        row = plant_initial_pumpkin_row()
        replace_dead_pumpkins(row)
        while True:
            navigation.go(ws - 1, 0)
            if get_entity_type() == Entities.Pumpkin:
                id = measure()
                navigation.go(0, ws - 1)
                if id == measure():
                    pet_the_piggy()
                    harvest()
                    break
        if num_items(Items.Pumpkin) > 1000000000 or num_items(Items.Carrot) < 1000000:
            break
    break
