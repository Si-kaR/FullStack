def dfs(graph, start):

    visited, stack = set(), [start]

    while stack:

        vertex = stack.pop()

        if vertex not in visited:

            visited.add(vertex)

            stack.extend(graph[vertex] - visited)

    return visited
graph = {'A':set(['B', 'C']), 
         
         'B':set(['B', 'C']),
         
         'C':set(['B', 'C']),
         
         'D':set(['B', 'C']),
         
         'E':set(['B', 'F']),
         
         'F':set(['C', 'E']),
         
         }



# #The code you provided is an implementation of Depth-First Search (DFS) algorithm in Python. DFS is used to traverse or search through a graph or tree data structure. Let's break down the code step by step:

# ```python
# def dfs(graph, start):
# ```

# This line defines a function named `dfs` that takes two arguments:
# - `graph`: This is a dictionary representing the graph you want to perform DFS on. In your example, the graph is represented as an adjacency list, where keys are nodes, and the values are sets of nodes representing the neighbors of each node.
# - `start`: This is the starting node from which the DFS traversal will begin.

# ```python
#     visited, stack = set(), [start]
# ```

# Here, two variables are initialized:
# - `visited`: This is an empty set that will be used to keep track of the nodes that have been visited during the DFS traversal.
# - `stack`: This is a list that will be used as a stack to keep track of the nodes that need to be explored. The initial node `start` is added to the stack.

# ```python
#     while stack:
# ```

# This line starts a `while` loop that will continue as long as there are nodes in the `stack` to explore.

# ```python
#         vertex = stack.pop()
# ```

# Inside the loop, the top node from the stack is popped (removed) and assigned to the variable `vertex`. This node will be explored next.

# ```python
#         if vertex not in visited:
# ```

# This `if` condition checks if the `vertex` has not been visited before.

# ```python
#             visited.add(vertex)
# ```

# If the `vertex` has not been visited, it is added to the `visited` set to mark it as visited.

# ```python
#             stack.extend(graph[vertex] - visited)
# ```

# The line above extends the `stack` with the neighbors of the `vertex` that have not been visited yet. It uses set difference (`-`) to filter out the neighbors that are already in the `visited` set, ensuring that only unvisited neighbors are added to the stack.

# The process continues until the stack becomes empty, at which point the DFS traversal is complete.

# ```python
#     return visited
# ```

# Finally, the function returns the `visited` set, which contains all the nodes visited during the DFS traversal.

# In your example, you provided a graph with one node 'A' and its neighbors 'B' and 'C'. If you call the `dfs` function with this graph and 'A' as the starting node, it will perform a DFS traversal and return the set of visited nodes, which will be all nodes in the graph in this case ('A', 'B', 'C').
# # 
# # #