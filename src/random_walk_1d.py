import random

x_particle = [0] #initially zero because particle starts at x = 0

for steps in range(100):
    random_step = random.randint(1, 2) # 1 being left and 2 being right
    if random_step == 1:
        new_x_pos = x_particle[steps] - 1 # will subtract 1 from the previous element of the array, going left
        x_particle.append(new_x_pos)
    elif random_step == 2:
        new_x_pos2 = x_particle[steps] + 1 # will add 1 to previous element of the array, going right
        x_particle.append(new_x_pos2)


print("x position over 100 steps", x_particle)
print("length of list:", len(x_particle))







