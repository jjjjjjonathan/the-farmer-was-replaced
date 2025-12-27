import navigation, farm_utils

clear()
ws = get_world_size()

def cheese(start, end, num):
    drones = []
    for x in range(start, end):
        for y in range(start, end):
            if x != num or y != num:
                drones.append(make_drone(x, y))
    do_a_flip()
    while True:
        plant(Entities.Bush)
        use_substance()
        counter = 0
        while measure():
            if get_entity_type() == Entities.Treasure:
                if counter > 3:
                    harvest()
                    counter = 0
                else:
                    use_substance()
                    counter += 1
					

def make_drone(x, y):
    def action():
        navigation.go(x,y)
        while True:
            while not measure():
                pass
            counter = 0
            while measure():
                if get_entity_type() == Entities.Treasure:
                    if counter > 3:
                        harvest()
                        counter = 0
                    else:
                        use_substance()
                        counter += 1
    return spawn_drone(action)

def use_substance():
    n = farm_utils.get_substance(4)
    use_item(Items.Weird_Substance, n)

def build_first_maze():
    cheese(0, 4, 0)

navigation.go(0,0)
spawn_drone(build_first_maze)
navigation.go(31, 31)
cheese(28, 32, 31)
