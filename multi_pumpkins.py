from navigation import go

ws = get_world_size()

pumpksize = 7
bordersize = 1
wide = 4
tall = 4

chunksize = pumpksize + bordersize

chunkqty = wide * tall

farm_width = wide * chunksize
farm_height = tall * chunksize
area = farm_width * farm_height

start_row = 0
start_col = 0
dead = 0

def next_chunk_up():
    if pumpksize % 2 == 1:
        for i in range(pumpksize):
            move(West)
        for j in range(bordersize + 1):
            move(North)
    else:
        for i in range(bordersize):
            move(North)

def next_chunk_right():
    global start_row
    if pumpksize % 2 == 1:
        ynow = get_pos_y()
        while ynow != start_row:
            move(South)
            ynow = get_pos_y()
        for j in range(bordersize):
            move(East)
    else:
        ynow = get_pos_y()
        while ynow != start_row:
            move(South)
            ynow = get_pos_y()
        for i in range(chunksize):
            move(East)

def till_right():
    for left in range(pumpksize):
        if get_ground_type() != Grounds.Soil:
            till()
        move(East)

def till_left():
    for right in range(pumpksize):
        move(West)
        if get_ground_type() != Grounds.Soil:
            till()
            
def till_full_chunk():
    if pumpksize % 2 == 0:
        for c in range(pumpksize / 2):
            till_right()
            move(North)
            till_left()
            move(North)
    else:
        for c in range((pumpksize - 1) / 2):
            till_right()
            move(North)
            till_left()
            move(North)
        till_right()
        
clear()
go(start_col, start_row)

for row in range(wide):
    for col in range(tall - 1):
        till_full_chunk()
        next_chunk_up()
    till_full_chunk()
    next_chunk_right()

go(start_col, start_row)
    
def pumk():
    plant(Entities.Pumpkin)
    
def plant_right():
    for left in range(pumpksize):
        pumk()
        move(East)

def plant_left():
    for r in range(pumpksize):
        move(West)
        pumk()
        
def plant_full_chunk():
    if pumpksize % 2 == 0:
        for c in range(pumpksize / 2):
            plant_right()
            move(North)
            plant_left()
            move(North)
    else:
        for c in range((pumpksize - 1) / 2):
            plant_right()
            move(North)
            plant_left()
            move(North)
        plant_right()
        
for row in range(wide):
    for col in range(tall - 1):
        plant_full_chunk()
        next_chunk_up()
    plant_full_chunk()
    next_chunk_right()
    
go(start_col, start_row)

def check_right():
    global dead  # keep it GLOBAL or the counter won't update!
    for r in range(pumpksize):
        status = get_entity_type()
        if status == Entities.Dead_Pumpkin:
            harvest()
            pumk()
            dead += 1
        move(East)
        
def check_left():
    global dead  # keep it GLOBAL!
    for r in range(pumpksize):
        move(West)
        status = get_entity_type()
        if status == Entities.Dead_Pumpkin:
            harvest()
            pumk()
            dead += 1
            
def gostartchunk():
    if pumpksize % 2 == 1:
        for i in range(pumpksize):
            move(West)
    else:
        move(South)
    for j in range(pumpksize - 1):
        move(South)

def initiate():
    do_a_flip()
    gostartchunk()
    harvest()
    plant_full_chunk()
            
def check_full_chunk():
    global dead  # keep it GLOBAL!
    dead = 0
    if pumpksize % 2 == 0:   # ----------------- if Pumpkin size is even
        for c in range(pumpksize/2):
            check_right()
            move(North)
            check_left()
            move(North)
    else:   # ---------------------------------- if Pumpkin size is odd 
        for c in range((pumpksize-1)/2):
            check_right()
            move(North)
            check_left()
            move(North)
        check_right()
#    print(dead) - to check if the counter works properly (remove # when debugging)
    if dead == 0:
        initiate()
        
while True:
    for row in range(wide):
        for col in range(tall - 1):
            check_full_chunk()
            next_chunk_up()
        check_full_chunk()
        next_chunk_right()
    go(start_col, start_row)
