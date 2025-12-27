def go(x, y, ws = get_world_size()):
    (x_now, y_now) = (get_pos_x(), get_pos_y())

    x_distance = (x - x_now) % ws

    if x_distance <= ws // 2:
        x_steps = x_distance
        x_direction = East
    else:
        x_steps = ws - x_distance
        x_direction = West

    y_distance = (y - y_now) % ws

    if y_distance <= ws // 2:
        y_steps = y_distance
        y_direction = North
    else:
        y_steps = ws - y_distance
        y_direction = South

    while x_steps > 0 or y_steps > 0:
        if x_steps >= y_steps and x_steps > 0:
            move(x_direction)
            x_steps -= 1
        elif y_steps > 0:
            move(y_direction)
            y_steps -= 1

def dinosaur_safe_move(direction):
    if can_move(direction):
        move(direction)
    else:
        change_hat(Hats.Golden_Cactus_Hat)
        change_hat(Hats.Dinosaur_Hat)
