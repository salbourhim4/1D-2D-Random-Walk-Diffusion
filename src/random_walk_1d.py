import random
import numpy as np

def random_walk(T: int) -> list: # A function that simulates a 1D random walk of a particle, T representing the number of steps

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

def N_walks(N: int, T: int) -> np.ndarray: #simulate N 1D random walks of T steps

    all_walks = np.empty((N, T+1), dtype = int) #empty 2D array of ints, N rows and T+1 columns

    for i in range(N):
        all_walks[i] = np.array(random_walk(T)) #adds the random_walk array to the 2D array
    
    return all_walks


def mean_position(A: np.ndarray, t: int) -> float: #  Function to calculate mean position, Takes the array of simulated walks and a time index as input

    N = len(A) # Number of walks simulated

    # Uses (1/N)(sum(xi(t))) 

    total = 0 #initial sum
    for i in range(N): #looping through each list element and adding the specific value at time t 
        total += A[i][t]
    
    return total / N

def MSD(A: np.ndarray, t: int) -> float: # Function to calculate Mean squared distance, takes an array of simulated walks and a time index as inputs

    N = len(A)

    # Uses (1/N)(sum(xi(t)))^2

    total = 0 #initial sum
    for i in range(N): #looping through each list element and adding and squaring the specific value at time t 
        total += (A[i][t])**2
    
    return total / N

#commit this before WRITING ANYTHING ELSE
def MSD_all_times(A: np.ndarray) -> np.ndarray: 

    return (A**2).mean(axis = 0)
