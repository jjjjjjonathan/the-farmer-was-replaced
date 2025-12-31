import navigation, farm_utils, drone_utils

clear()
ws = get_world_size()
change_hat(Hats.Golden_Cactus_Hat)
farm_utils.till_all()

def plant_cacti_row():
    for _ in range(ws):
        plant(Entities.Cactus)
        move(East)

def sort_cacti_row():
    y = get_pos_y()
    for x in range(1, ws):
        navigation.go(x, y)
        left = measure(West)
        curr = measure()
        x_now = get_pos_x()
        while left < curr and x_now != 0:
            swap(West)
            move(West)
            left = measure(West)
            curr = measure()
            x_now = get_pos_x()

def plant_and_sort_cacti_row():
    change_hat(Hats.Golden_Cactus_Hat)
    plant_cacti_row()
    sort_cacti_row()

def sort_cacti_column():
    change_hat(Hats.Golden_Cactus_Hat)
    x = get_pos_x()
    for y in range(1, ws):
        navigation.go(x,y)
        bottom = measure(South)
        curr = measure()
        y_now = get_pos_y()
        while bottom < curr and y_now != 0:
            swap(South)
            move(South)
            bottom = measure(South)
            curr = measure()
            y_now = get_pos_y()

while True:
    navigation.go(0,0)
    drone_utils.spawn_drones(plant_and_sort_cacti_row, North)
    navigation.go(0,0)
    drone_utils.spawn_drones(sort_cacti_column, East)
    harvest()
