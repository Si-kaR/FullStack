'''
Name : Robert Sika
ID   : 89212025


Assignment | Search Problems
Due        | 16 Sep 23:59 | Today by 23:59 

Points     | 20 
File types | zip 
Submitting | file upload 
Available  | 31 Aug at 17:00 - 17 Sep at 23:59


Task: 

    The following is a representation of a search problem, where A is the start node and G is the goal. There is also a heuristics h which is defined in the table. Note that h(B) is unknown.
    0 ≤ h(B) ≤ 6, since the minimal cost from B to G is 6. Use Python to implement the following:

    1. Implement DFS and show the path from the start state to the goal state [5 Points]
    2. Implement an algorithm that shows all possible paths from the start to the final node [5 Points]
    3. Implement the Greedy Best First Search and show the path from A to G. Use the path cost (edge weights) between nodes on the graph as your heuristics.   [5 Points]
    4. Implement the A* algorithm and show the optimum path it will choose from A to G [5 Points]

'''

#Defining Graph using Dictionary
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('C', 2)],
    'C': [('E', 5)],
    'D': [('G', 4),('F', 2)],
    'E': [('G', 3)],
    'F': [('G', 1)]
}

# Define heuristic values for each node to estimate the cost to reach the goal 'G'.
heuristics = {
    'A': 5,
    #minimal estimated path cost from B to G is 6 via (D) or via (D and F)
    'B': 6, 
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0
}

# Heuristic estimated values based on the minimum path cost 
# to reach the goal 'G' from from every other node.
#Defining Heuristics_gbfs
heuristics_gbfs = { #Below are minimum costs for the following paths;
    'A': 7,   #from (A) to ((G))= 7 ; via (B and D) or via (C and E) or via (B, D, and F)
    'B': 6,   #from (B) to (G) = 6 ; via (D) or via (D and F).
    'C': 8,   #from (C) to (G) = 8 ; via (E)
    'D': 3,   #from (D) to (G) = 4 ;
    'E': 3,   #from (E) to (G) = 3 ; 
    'F': 1,   #from (F) to (G) = 1 ;
    'G': 0    # Heuristic value of goal node (node) = 0; thus from goal to itself ; tackling the In(G) Go(G) challenge
}

#Setting initializers for the algorithms
start = 'A' # Setting initial node
goal = 'G' # Setting goal node


'''Question 1'''
'''Implement Depth - First Algorithm to find solution: Sequence of actions from start to goal'''
def dfs(graph, start, goal):
    stack = [(start, [start])] # Initialize stack with start node and its path 
    visited = set() # Keep track of visited nodes to avoid re-exploring them and loop path 
    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            for neighbor, _ in graph[node]:
                stack.append((neighbor, path + [neighbor])) # Adding neighbors to stack
    return None

print("")
print(dfs(graph, start, goal))




'''Question 2'''
'''Function to find all paths from start to goal in the graph.'''
def all_paths(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return [path]
    paths = []
    for neighbor, _ in graph[start]:
        if neighbor not in path:
            new_paths = all_paths(graph, neighbor, goal, path)
            for p in new_paths:
                paths.append(p)
    return paths

print("")
print(all_paths(graph, start, goal))




'''Question 3'''
'''Implementing Greedy Best-First Search algorithm.'''
def greedy_best_first_search(graph, start, goal, heuristics):

    open_list = [(start, heuristics[start])] # Initialize the open list (Frontiers ; Set of Leaves ; Candidates for expansion) with the start node and its heuristic value.
    closed_set = set() # Keep track of visited nodes to avoid re-exploring them and loop path 
    visited_path_dict  = {} # Storing path information; History

    while open_list:
        node, _ = min(open_list, key=lambda x: x[1]) # Choosing the node with the lowest heuristic value.
        open_list.remove((node, heuristics[node])) 

        if node == goal:
            return reconstruct_path(start, goal, visited_path_dict )

        closed_set.add(node)

        for neighbor, _ in graph[node]:
            if neighbor not in closed_set:
                if neighbor not in (item[0] for item in open_list):
                    visited_path_dict [neighbor] = node
                    open_list.append((neighbor, heuristics[neighbor]))

    return None


# Helper function to reconstruct the path from start to goal using the visited_path_dict  dictionary.
def reconstruct_path(start, goal, visited_path_dict ):
    path = [goal]
    while goal != start:
        goal = visited_path_dict [goal]
        path.insert(0, goal)
    return path

print("")
print(greedy_best_first_search(graph, start, goal, heuristics_gbfs))




'''Question 4'''
'''Implementing A* algorithm to find the optimal path from start to goal.'''
def astar(graph, start, goal, heuristics):

    visited = set()
    queue = [(heuristics[start], 0, [start])] # Initialize the queue with the start node and its heuristic value.
    while queue:
        (h, cost, path) = queue.pop(0)
        node = path[-1]
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    g = cost + weight
                    h = heuristics[neighbor]
                    f = g + h
                    queue.append((f, g, path + [neighbor]))
                    queue.sort() # Sort the queue by the total estimated cost.
    return None

print("")
print(astar(graph, start, goal, heuristics))