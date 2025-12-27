import navigation, farm_utils

clear()
set_world_size(5)
ws = get_world_size()
farm_utils.till_all(ws)

while True:
    navigation.go(0,0)
    harvest()
    farm_utils.maintain_water_level()
    plant(Entities.Tree)
    use_item(Items.Fertilizer)
    companion, (x, y) = get_companion()
    navigation.go(x, y)
    harvest()
    plant(companion)
    if num_items(Items.Weird_Substance) > 100000000:
        break
