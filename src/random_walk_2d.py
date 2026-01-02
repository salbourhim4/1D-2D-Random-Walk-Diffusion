import random
import numpy as np
import matplotlib.pyplot as plt

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

    return all_walks # returns a 3D array

def MSD_all_times_2D(A: np.ndarray) -> np.ndarray: # Calculates MSD across all times 
    return (A**2).sum(axis=1).mean(axis=0) 

def plot_diffusion_2D(N: int, T: int): 

    # generates random walks and MSD array
    walks = N_walks_2D(N, T)
    msd = MSD_all_times_2D(walks)

    theoretical_time = np.arange(T+1) # Array of time values, [0, 1, 2, ...]
    
    # create scatter plot of msd values
    plt.figure(figsize=(10,6))
    plt.scatter(theoretical_time, msd, color='blue', s=30, alpha=0.7, label='Simulated MSD', zorder=3)

    # create plot of best fit (In 2D: MSD = 4Dt = 2t when D=0.5)
    plt.plot(theoretical_time, 2*theoretical_time, 'r-', linewidth=2, label='Theoretical (MSD = 2t)', zorder = 2)

    # creates grid and labels
    plt.xlabel('Time (steps)', fontsize=12)
    plt.ylabel('Mean Squared Displacement', fontsize=12)
    plt.title('MSD vs Time for 2D Random Walk', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.tight_layout()
    plt.show()

    # calculate diffusion coefficients
    slope = np.polyfit(theoretical_time[1:], msd[1:], 1)[0]
    diffusion_sim = slope/4

    return f"Simulate diffusion coefficient D = {diffusion_sim:.4f} \nTheoretical diffusion coefficient D = 0.5"
