# 1D-2D Random Walk Diffusion Simulation

## Overview
This project uses Monte Carlo simulations of unbiased random walks to demonstrate diffusion by computing the mean squared displacement (MSD) and extracting the diffusion coefficient. The simulations verify theoretical scaling laws numerically, showing that MSD ∝ t for both 1D and 2D random walks

## Key Results
- Demonstrates that mean squared displacement scales linearly with time
- Extracts diffusion coefficients from simulated data
- Shows convergence to theoretical predictions as the number of walks increases
- Validates Einsteins relation for Brownian motion

## Features 
- 1D Random Walk Simulation: Particle moves left or right with equal probability
- 2D Random Walk Simulation: Particle moves in four cardinal directions with equal probability
- MSD Calculation: Computes mean squared displacement across multiple walks
- Visualization: Plots MSD vs time with theoretical predictions overlay
- Diffusion Coefficient Extraction: Calculates diffusion coefficient from the slope of the MSD vs time graph

## Requirements
```
numpy
matplotlib
```

## Installation
```bash
git clone https://github.com/salbourhim4/1D-2D-Random-Walk-Diffusion.git
cd 1D-2D-Random-Walk-Diffusion
```

Install dependencies:
```bash
pip install numpy matplotlib
```

## Usage

### Basic 1D Simulation
```python
import numpy as np
import matplotlib.pyplot as plt
from random_walk import *

# Run 1000 walks of 100 steps each
N = 1000  # Number of walks
T = 100   # Number of steps

walks = N_walks(N, T)
msd = MSD_all_times(walks)

# Plot results
plot_diffusion(N, T)
```

### Basic 2D Simulation
```python
# Run 1000 2D walks of 100 steps each
walks_2d = N_walks_2D(N, T)
msd_2d = MSD_all_times_2D(walks_2d)

# Plot results
plot_diffusion_2D(N, T)
```

## Functions

### 1D Random Walk Functions
- `random_walk(T)`: Simulates a single 1D random walk of T steps
- `N_walks(N, T)`: Generates N independent 1D random walks
- `mean_position(A, t)`: Calculates mean position at time t
- `MSD(A, t)`: Calculates mean squared displacement at time t
- `MSD_all_times(A)`: Calculates MSD for all time steps efficiently
- `plot_diffusion(N, T)`: Generates MSD vs time plot with diffusion coefficient

### 2D Random Walk Functions
- `rand_walk_2D(T)`: Simulates a single 2D random walk of T steps
- `N_walks_2D(N, T)`: Generates N independent 2D random walks
- `MSD_all_times_2D(A)`: Calculates 2D MSD for all time steps
- `plot_diffusion_2D(N, T)`: Generates 2D MSD vs time plot

## Theoretical Background

### 1D Random Walk
- Diffusion coefficient: **D = 0.5** (for unit step size)
- MSD relation: **MSD = 2Dt = t**
- Theoretical slope: **1**

### 2D Random Walk
- Diffusion coefficient: **D = 0.25** (for unit step size)
- MSD relation: **MSD = 4Dt = t**
- Theoretical slope: **1**

### Convergence
Increasing N (number of walks) reduces statistical noise and improves agreement with theory. Increasing T (number of steps) extends the time range for verification.

## Example Results

The simulations demonstrate:
1. **Linear scaling**: MSD grows linearly with time (MSD ∝ t)
2. **Theoretical agreement**: Simulated diffusion coefficients match theoretical predictions
3. **Statistical convergence**: Larger N produces smoother curves closer to theory

## Project Structure
```
1D-2D-Random-Walk-Diffusion/
│
├── random_walk.py          # Main simulation code
├── README.md               # This file
└── examples/               # Example plots and results (optional)
```

## Future Extensions
- [ ] Add 3D random walk simulation
- [ ] Implement biased random walks (drift)
- [ ] Add animation of random walk trajectories
- [ ] Explore different step size distributions
- [ ] Compare with analytical solutions

## Contributing
Feel free to open issues or submit pull requests for improvements!

## License
This project is licensed under the terms of the MIT license.

## Author
Salaheddine Bourhim

## Acknowledgments
This project demonstrates fundamental concepts in statistical mechanics and Brownian motion, following the work of Einstein and Smoluchowski on diffusion theory.

