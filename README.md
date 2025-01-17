# Description

Simulation of one hunter and one or multiple prey. This project has [C++ version](https://github.com/maxboro/hunter-killer-cpp).
The hunter and the prey move randomly to a nearby cell or pass their turn. The hunter kills the prey if they are in the same cell.

# Session examples

## Session example (wo full grid display)

```terminal
Simulation parameters: {'n_prey': 5, 'n_steps': 5, 'grid_size_x': 3, 'grid_size_y': 3, 'show_grid': False}
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

## Session example (with full grid display)

```terminal
Simulation parameters: {'n_prey': 6, 'n_steps': 5, 'grid_size_x': 3, 'grid_size_y': 3, 'show_grid': True}
Prey_0 at [0, 2]. Is alive.
Prey_1 at [0, 1]. Is alive.
Prey_2 at [0, 1]. Is alive.
Prey_3 at [1, 1]. Is alive.
Prey_4 at [2, 1]. Is alive.
Prey_5 at [0, 0]. Is alive.
Hunter at [1, 0]
P|H|
P|P|P
P| |
----------------------------
Prey_0 at [0, 1]. Is alive.
Prey_1 at [0, 1]. Is alive.
Prey_2 at [0, 1]. Is alive.
Prey_3 at [1, 1]. Is alive.
Prey_4 at [1, 1]. Is alive.
Prey_5 at [0, 0]. Is alive.
Hunter at [1, 0]
P|H|
P|P|
 | |
----------------------------
Prey_0 at [0, 2]. Is alive.
Prey_1 at [0, 1]. Is alive.
Prey_2 at [0, 1]. Is alive.
Prey_3 at [2, 1]. Is alive.
Prey_4 at [1, 1]. Is alive.
Prey_5 at [0, 0]. Is alive.
Hunter at [1, 0]
P|H|
P|P|P
P| |
----------------------------
Prey_4 is killed.
Prey_0 at [0, 2]. Is alive.
Prey_1 at [0, 1]. Is alive.
Prey_2 at [0, 1]. Is alive.
Prey_3 at [2, 1]. Is alive.
Prey_4 at [1, 1]. Is dead
Prey_5 at [0, 0]. Is alive.
Hunter at [1, 1]
P| |
P|H|P
P| |
----------------------------
Prey_0 at [0, 2]. Is alive.
Prey_1 at [1, 1]. Is alive.
Prey_2 at [0, 0]. Is alive.
Prey_3 at [2, 1]. Is alive.
Prey_4 at [1, 1]. Is dead
Prey_5 at [0, 0]. Is alive.
Hunter at [1, 0]
P|H|
 |X|P
P| |
----------------------------
Prey_0 at [0, 2]. Is alive.
Prey_1 at [1, 0]. Is alive.
Prey_2 at [0, 0]. Is alive.
Prey_3 at [2, 1]. Is alive.
Prey_4 at [1, 1]. Is dead
Prey_5 at [0, 1]. Is alive.
Hunter at [2, 0]
P|P|H
P|X|P
P| |
```

# How to run

## Simulation

```bash
python main.py
```

## Unit tests

```bash
python test_main.py
```

# Settings

Can be changed in `settings.txt`.

- n_prey (int: default 2) - Number of prey
- n_steps (int: default 20) - Number of simulation steps
- grid_size_x (int: default 5) - Grid size in X dimension
- grid_size_y (int: default 5) - Grid size in Y dimension
- show_grid (int: default 1) - Flag to show grid
