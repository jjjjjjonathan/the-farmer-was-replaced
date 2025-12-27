import navigation, farm_utils, constants

ws = get_world_size()

def plant_sunflower_row():
    for _ in range(ws):
        farm_utils.maintain_water_level()
        plant(Entities.Sunflower)
        move(East)

def farm_sunflower_row(petal_num):
    for _ in range(ws):
        if measure() == petal_num and can_harvest():
            harvest()
        move(East)

def farm():
    navigation.go(0,0)
    if get_ground_type() != Grounds.Soil:
        farm_utils.till_all(ws)
    while num_items(Items.Power) < constants.MAX_POWER:
        navigation.go(0,0)
        farm_utils.spawn_drones(plant_sunflower_row, North, ws)
        navigation.go(0,0)
        for i in range(15, 6, -1):
            def task():
                farm_sunflower_row(i)
            farm_utils.spawn_drones(task, North, ws)
    