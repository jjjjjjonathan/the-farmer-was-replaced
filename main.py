from constants import WS
import farm_utils, sunflowers, grass, carrots, wood

ws = WS

clear()

farm_funcs = [wood.farm, grass.farm, carrots.farm]

last_i = -1

def main():
    global last_i
    start = get_time()

    # while get_time() - start <= 11111:
    while True:
        while not farm_utils.enough_power():
            sunflowers.farm()
        while farm_utils.enough_power():
            i = farm_utils.random_index(len(farm_funcs))

            # don't re-farm the last farmed item
            while i == last_i:
                i = farm_utils.random_index(len(farm_funcs))
            farm_funcs[i]()

            last_i = i
            farm_utils.clean()

main()
