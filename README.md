# Description
Simulation of one hunter and one or multiple prey.

# Session example
```terminal
Simulation parameters: {'n_prey': 5, 'n_steps': 5, 'grid_size_x': 3, 'grid_size_y': 3}
Prey_0 at [0, 2]. Is alive.
Prey_1 at [0, 1]. Is alive.
Prey_2 at [0, 1]. Is alive.
Prey_3 at [1, 1]. Is alive.
Prey_4 at [2, 1]. Is alive.
Hunter at [0, 0]
----------------------------
Prey_2 is killed.
Prey_0 at [0, 2]. Is alive.
Prey_1 at [0, 1]. Is alive.
Prey_2 at [0, 0]. Is dead
Prey_3 at [1, 0]. Is alive.
Prey_4 at [2, 1]. Is alive.
Hunter at [0, 0]
----------------------------
Prey_1 is killed.
Prey_2 is killed.
Prey_0 at [0, 2]. Is alive.
Prey_1 at [0, 0]. Is dead
Prey_2 at [0, 0]. Is dead
Prey_3 at [1, 0]. Is alive.
Prey_4 at [2, 1]. Is alive.
Hunter at [0, 0]
----------------------------
Prey_0 at [0, 2]. Is alive.
Prey_1 at [0, 0]. Is dead
Prey_2 at [0, 0]. Is dead
Prey_3 at [0, 0]. Is alive.
Prey_4 at [1, 1]. Is alive.
Hunter at [1, 0]
```

# How to run 
```bash
python hunter_killer.py --n_prey=2 --n_steps=20 --grid_size_x=30 --grid_size_y=30 --show_grid
```

# Parameters
- n_prey (int: default 2) - Number of prey
- n_steps (int: default 20) - Number of simulation steps
- grid_size_x (int: default 30) - Grid size in X dimention
- grid_size_y (int: default 30) - Grid size in Y dimention
- show_grid (bool: default false) - Flag to show grid
