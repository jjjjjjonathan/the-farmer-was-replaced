import navigation

hats = [Hats.Cactus_Hat, Hats.Carrot_Hat, Hats.Gray_Hat, Hats.Green_Hat, Hats.Golden_Cactus_Hat]
navigation.go(4,4)

for i in range(5):
    def task():
        change_hat(hats[i])
        navigation.go(i, 0)
        while True:
            pet_the_piggy()
    spawn_drone(task)
