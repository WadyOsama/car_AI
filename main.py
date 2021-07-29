import AiSearch
import random


def print_grid(grid):
    s = ""
    for cell in grid:
        if cell == 0: s += str(' ')
        if cell == 1: s += str('x')
        if cell == 2: s += str('V')
        if cell == 3: s += str('G')
        if cell == 4: s += str('D')
    print(
        '-' * 22 + '\n' +
        '| ' + s[0] + ' | ' + s[1] + ' | ' + s[2] + ' | ' + s[3] + ' | ' + s[4] + ' |' + '\n' +
        '-' * 22 + '\n' +
        '| ' + s[5] + ' | ' + s[6] + ' | ' + s[7] + ' | ' + s[8] + ' | ' + s[9] + ' |' + '\n' +
        '-' * 22 + '\n' +
        '| ' + s[10] + ' | ' + s[11] + ' | ' + s[12] + ' | ' + s[13] + ' | ' + s[14] + ' |' + '\n' +
        '-' * 22 + '\n' +
        '| ' + s[15] + ' | ' + s[16] + ' | ' + s[17] + ' | ' + s[18] + ' | ' + s[19] + ' |' + '\n' +
        '-' * 22 + '\n' +
        '| ' + s[20] + ' | ' + s[21] + ' | ' + s[22] + ' | ' + s[23] + ' | ' + s[24] + ' |' + '\n' +
        '-' * 22

    )


def vehicle_location(grid):
    for i in range(len(grid)):
        if grid[i] == 2:
            return i
        if grid[i] == 4:
            return i


def obstacles_location(grid):
    obstacles = []
    for i in range(len(grid)):
        if grid[i] == 1:
            obstacles.append(i)
    return obstacles


def goal_location(grid):
    for i in range(len(grid)):
        if grid[i] == 3:
            return i
        if grid[i] == 4:
            return i


def actions_fun(grid):
    vehicle = vehicle_location(grid)
    obstacle = obstacles_location(grid)
    actions = []
    if vehicle not in [0, 1, 2, 3, 4, obstacle[0] + 5, obstacle[1] + 5, obstacle[2] + 5,
                       obstacle[3] + 5]: actions.append('^')
    if vehicle not in [20, 21, 22, 23, 24, obstacle[0] - 5, obstacle[1] - 5, obstacle[2] - 5,
                       obstacle[3] - 5]: actions.append('v')
    if vehicle not in [0, 5, 10, 15, 20, obstacle[0] + 1, obstacle[1] + 1, obstacle[2] + 1,
                       obstacle[3] + 1]: actions.append('<')
    if vehicle not in [4, 9, 14, 19, 24, obstacle[0] - 1, obstacle[1] - 1, obstacle[2] - 1,
                       obstacle[3] - 1]: actions.append('>')
    return actions


def move_vehicle(source_grid, action):
    next_grid = source_grid[:]
    vehicle = vehicle_location(source_grid)
    goal = goal_location(grid)
    if (action == '>') and (vehicle + 1 != goal):
        next_grid[vehicle], next_grid[vehicle + 1] = next_grid[vehicle + 1], next_grid[vehicle]
    elif (action == '<') and (vehicle - 1 != goal):
        next_grid[vehicle], next_grid[vehicle - 1] = next_grid[vehicle - 1], next_grid[vehicle]
    elif (action == '^') and (vehicle - 5 != goal):
        next_grid[vehicle], next_grid[vehicle - 5] = next_grid[vehicle - 5], next_grid[vehicle]
    elif (action == 'v') and (vehicle + 5 != goal):
        next_grid[vehicle], next_grid[vehicle + 5] = next_grid[vehicle + 5], next_grid[vehicle]
    else:
        next_grid[vehicle] = 0
        next_grid[goal] = 4
    return next_grid


def goal_reach(grid):
    for i in grid:
        if i == 4:
            return True
    return False


def move_cost(grid, action, dir):
    if action == dir:
        return 1
    if (action == 'v' and dir == '^') or (action == '^' and dir == 'v') or (action == '<' and dir == '>') or (
            action == '>' and dir == '<'):
        return 3
    return 2


def h1(grid):
    vehicle = vehicle_location(grid)
    goal = goal_location(grid)
    h = abs(int(vehicle / 5) - int(goal / 5)) + abs(int(vehicle % 5) - int(goal % 5))
    return h


def computer_solve(grid, strategy, steps=False):
    s = AiSearch.solve(strategy, grid, actions_fun, move_vehicle, goal_reach, move_cost, h1)
    print(strategy, ": ")
    for i in s:
        print(i, ": ", s[i])
    print('\n')
    if steps:
        sol_grid = grid[:]
        print_grid(sol_grid)
        for action in s['solution']:
            sol_grid = move_vehicle(sol_grid, action)
            print_grid(sol_grid)


# 0 for empty cell, 1 for non-empty, 2 for the car, 3 for the goal, 4 for reaching destination
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 3]
random.shuffle(grid)


computer_solve(grid, 'BFS')
computer_solve(grid, 'DFS')
computer_solve(grid, 'UCS')
computer_solve(grid, 'Greedy')
computer_solve(grid, 'Astar')
