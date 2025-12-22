import random

def random_walk(T): # A function that simulates a 1D random walk of a particle, T representing the number of steps

    x_particle = [0] #initially zero because particle starts at x = 0

    for steps in range(T):
        random_step = random.randint(1, 2) # 1 being left and 2 being right
        if random_step == 1:
            new_x_pos = x_particle[steps] - 1 # will subtract 1 from the previous element of the array, going left
            x_particle.append(new_x_pos)
        elif random_step == 2:
            new_x_pos2 = x_particle[steps] + 1 # will add 1 to previous element of the array, going right
            x_particle.append(new_x_pos2)
    return x_particle


print("x position over 100 steps", random_walk(100))
print("length of list:", len(random_walk(100)))







