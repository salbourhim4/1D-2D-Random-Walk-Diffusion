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

