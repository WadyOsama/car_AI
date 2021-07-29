#def solve(strategy, initial_state, env, get_actions, get_state, isgoal, compute_cost, heuristic):
def solve(strategy, initial_state, get_actions, get_state, isgoal, compute_cost=None, heuristic=None):
    fringe = []
    visited = []
    fringe.append(init_node(strategy, initial_state))
    while len(fringe) > 0:
        current_node = fringe.pop(select_node(fringe, strategy))
        if current_node['state'] in visited: continue
        visited.append(current_node['state'])
        # print(current_node)
        if isgoal(current_node['state']):
            solution = {}
            solution['solution'] = current_node['path']
            if strategy in ('UCS', 'Astar'): solution['cost'] = current_node['cost']
            solution['expanded nodes'] = len(visited)
            return solution
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_state = get_state(current_node['state'], action)
            next_node = add_node(strategy, next_state, current_node, action, compute_cost, heuristic)
            fringe.append(next_node)
    solution = {'solution': 'there is no way to the goal',
                'expanded nodes': len(visited)
                }
    return solution


def init_node(strategy, initial_state):
    initial_node = {}
    initial_node['state'] = initial_state
    initial_node['path'] = []
    initial_node['direction'] = '>'
    if strategy in ('UCS', 'Astar'): initial_node['cost'] = 0
    if strategy == 'Greedy': initial_node['h'] = 0
    if strategy == 'Astar': initial_node['f'] = 0
    return initial_node


def select_node(fringe, strategy):
    if strategy == 'DFS': return -1
    if strategy == 'BFS': return 0
    if strategy == 'UCS': return get_min(fringe, 'cost')
    if strategy == 'Greedy': return get_min(fringe, 'h')
    if strategy == 'Astar': return get_min(fringe, 'f')


def add_node(strategy, next_state, current_node, action, compute_cost, heuristic):
    next_node = {}
    next_node['state'] = next_state
    next_node['path'] = current_node['path'][:]
    next_node['path'].append(action)
    #next_node['path'] =[current_node['path'],action]
    next_node['direction'] = action
    if strategy in ('UCS', 'Astar'):
        next_node['cost'] = current_node['cost'] + compute_cost(current_node['state'], action,
                                                                current_node['direction'])
    if strategy == 'Greedy':
        next_node['h'] = heuristic(next_node['state'])
    if strategy == 'Astar':
        next_node['f'] = heuristic(next_node['state']) + next_node['cost']
    return next_node


def get_min(fringe, key):
    index_min = 0
    for i in range(1, len(fringe)):
        if fringe[i][key] < fringe[index_min][key]:
            index_min = i
    return index_min
