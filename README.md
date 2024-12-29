# Destription
Simulation of one hunter and one or multiple prey.

# Session example
```terminal
----------------------------
Player Prey_0 at [3, 18]
Player Prey_1 at [27, 24]
Hunter at [24, 3]
----------------------------
Player Prey_0 at [3, 17]
Player Prey_1 at [27, 24]
Hunter at [24, 2]
----------------------------
Player Prey_0 at [3, 17]
Player Prey_1 at [28, 24]
Hunter at [24, 1]
----------------------------
Player Prey_0 at [3, 16]
Player Prey_1 at [27, 24]
Hunter at [23, 1]
----------------------------
Player Prey_0 at [3, 15]
Player Prey_1 at [27, 24]
Hunter at [23, 0]
----------------------------
Player Prey_0 at [3, 15]
Player Prey_1 at [27, 23]
Hunter at [22, 0]
----------------------------
Player Prey_0 at [3, 15]
Player Prey_1 at [27, 23]
Hunter at [22, 1]
```

# How to run 
```bash
python hunter_killer.py --n_prey=2 --n_steps=20 --grid_size_x=30 --grid_size_y=30
```

# Parameters
- n_prey (int: default 2) - Number of prey
- n_steps (int: default 20) - Number of simulation steps
- grid_size_x (int: default 30) - Grid size in X dimention
- grid_size_y (int: default 30) - Grid size in Y dimention

