def wait_for_all_drones(drone_set):
    while len(drone_set) > 0:
        removed_drones = []
        for drone in drone_set:
            if has_finished(drone):
                removed_drones.append(drone)
        for removed_drone in removed_drones:
            drone_set.remove(removed_drone)

def spawn_drones(callback, direction, drone_num = max_drones()):
    drones = set()
    for _ in range(drone_num):
        drone = None
        if num_drones() < drone_num:
            drone = spawn_drone(callback)
        if not drone:
            callback()
        else:
            drones.add(drone)
        move(direction)
    wait_for_all_drones(drones)
