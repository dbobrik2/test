import random

value_1 = random.randint(1, 6)
value_2 = random.randint(1, 6)

player_1 = value_1 + value_2

value_3 = random.randint(1, 6)
value_4 = random.randint(1, 6)

player_2 =  value_3 + value_4

if player_1 > player_2:
    print("WIN 1 PLAYER!!!")
elif player_1 < player_2:
    print("WIN 2 PLAYER!!!")
else:
    print("DRAAAAAAW!!!")