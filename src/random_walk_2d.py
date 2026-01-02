import random
import numpy as np

def rand_walk_2D(T: int) -> list: #function to simulate a single 2d random walk of steps T

    # Initial positions at origin (0,0)
    x_init = [0] 
    y_init = [0]
    
    # List to define every possible direction to be taken each 1/4 chance of happening
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # left, down, right, up
    
    # simulates the walk
    for steps in range(T):
        x, y = random.choice(directions)
        
        x_init.append(x_init[steps] + x)
        y_init.append(y_init[steps] + y)
    
    return [x_init, y_init]

def N_walks_2D(N: int, T: int) -> np.ndarray: # function to simulate N 2D random walks of steps T

    all_walks = np.empty((N, 2, T+1), dtype=int) # creates an empty 3D array of height N, width 2, and depth T+1
    # We use 2 for the second dimension of the 3D array to differentiate between the two dimensions x and y


    for i in range(N):
        all_walks[i] = np.array(rand_walk_2D(T))

    return all_walks # returns a 1D array


