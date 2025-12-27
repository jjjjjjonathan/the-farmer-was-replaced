import farm_utils

dirs = [East, South, West, North]
dirs_index = {East:0, South:1, West:2, North:3}

def get_right_dir(dir):
    return dirs[(dirs_index[dir] + 1) % 4]

def get_left_dir(dir):
    return dirs[(dirs_index[dir] - 1) % 4]

clear()
ws = get_world_size()

while True:
    plant(Entities.Bush)
    substance = farm_utils.get_substance(ws)
    use_item(Items.Weird_Substance, substance)
    dir = North

    while True:
        if can_move(get_right_dir(dir)):
            dir = get_right_dir(dir)
            move(dir)
        else:
            dir = get_left_dir(dir)
        if get_entity_type() == Entities.Treasure:
            harvest()
            break
