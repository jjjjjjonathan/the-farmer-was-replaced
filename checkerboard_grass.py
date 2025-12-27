import farm_utils, navigation

clear()
set_world_size(8)
ws = get_world_size()

def harvest_hay(x,y):
    navigation.go(x,y)
    while True:
        if can_harvest():
            harvest()
        farm_utils.maintain_water_level()

def plant_friends():
    farm_utils.plant_friends(Entities.Bush, ws)

def farm():
    navigation.go(0,0)
    farm_utils.spawn_drones(plant_friends, North, ws)
    for x in range(0, ws, 2):
        for y in range(0, ws, 2):
            def task():
                harvest_hay(x,y)
            spawn_drone(task)
    
    for x in range(1, ws, 2):
        for y in range(1, ws, 2):
            if x == ws - 1 and y == ws - 1:
                break
            def task():
                harvest_hay(x,y)
            spawn_drone(task)
    harvest_hay(15,15)


farm()
