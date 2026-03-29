import heapq
import time
from collections import deque

# Graph definition: {Node: {Neighbor: Edge Weight}}
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'G': 5},
    'D': {'G': 1},
    'G': {}
}

# Heuristic values (estimated distance to goal 'G')
heuristic = {'A': 6, 'B': 4, 'C': 3, 'D': 1, 'G': 0}

# A* Algorithm
def astar(start, goal):
    start_time = time.time()
    # Priority Queue stores (priority, current_node)
    pq = [(0 + heuristic[start], start)]
    cost = {start: 0}
    
    while pq:
        # We don't need the priority value once popped, hence the underscore
        _, n = heapq.heappop(pq)
        
        if n == goal: 
            break
            
        for nb, w in graph[n].items():
            new_cost = cost[n] + w
            if nb not in cost or new_cost < cost[nb]:
                cost[nb] = new_cost
                priority = new_cost + heuristic[nb]
                heapq.heappush(pq, (priority, nb))
                
    return cost.get(goal, float('inf')), time.time() - start_time

# BFS Algorithm
def bfs(start, goal):
    start_time = time.time()
    queue = deque([start])
    visited = {start}
    
    while queue:
        n = queue.popleft()
        if n == goal: 
            break
        for nb in graph[n]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
                
    return time.time() - start_time

# Execute and Print Results
a_cost, a_time = astar('A', 'G')
b_time = bfs('A', 'G')

print("-" * 30)
print(f"A* Results:")
print(f"  Total Cost: {a_cost}")
print(f"  Execution Time: {a_time:.8f} seconds")
print("-" * 30)
print(f"BFS Results:")
print(f"  Execution Time: {b_time:.8f} seconds")
print("-" * 30)