import navigation

clear()
change_hat(Hats.Dinosaur_Hat)
ws = get_world_size()

while True:
    for x in range(ws):
        if x % 2 == 0:
            target_y = ws - 1
        else:
            target_y = 1
        
        while get_pos_y() != target_y:
            if target_y > get_pos_y():
                navigation.dinosaur_safe_move(North)
            else:
                navigation.dinosaur_safe_move(South)
        
        if x < ws - 1:
            move(East)

    while get_pos_y() != 0:
        navigation.dinosaur_safe_move(South)

    while get_pos_x() != 0:
        navigation.dinosaur_safe_move(West)
