import random
import numpy as np

def random_walk(T): # A function that simulates a 1D random walk of a particle, T representing the number of steps

    x_particle = [0] #initially zero because particle starts at x = 0
    # due to this initial value of zero, every array of random_walk will have length of T+1

    for steps in range(T):
        random_step = random.randint(1, 2) # 1 being left and 2 being right
        if random_step == 1:
            new_x_pos = x_particle[steps] - 1 # will subtract 1 from the previous element of the array, going left
            x_particle.append(new_x_pos)
        elif random_step == 2:
            new_x_pos2 = x_particle[steps] + 1 # will add 1 to previous element of the array, going right
            x_particle.append(new_x_pos2)
    return x_particle

def N_walks(N, T): #simulate N 1D random walks of T steps

    all_walks = np.empty((N, T+1), dtype = int) #empty 2D array of ints, N rows and T+1 columns

    for i in range(N):
        all_walks[i] = np.array(random_walk(T)) #adds the random_walk array to the 2D array
    
    return all_walks



    
# print("x position over 100 steps", random_walk(100))
# print("length of list:", len(random_walk(100)))







