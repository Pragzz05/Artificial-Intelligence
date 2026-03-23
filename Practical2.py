from collections import deque

def water_jug_problem(cap_a=4, cap_b=3, goal=2):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        # Goal condition
        if b == goal and a == 0:
            return path

        # Possible moves
        moves = [
            (cap_a, b),  # Fill jug A
            (a, cap_b),  # Fill jug B
            (0, b),      # Empty jug A
            (a, 0),      # Empty jug B
            (a - min(a, cap_b - b), b + min(a, cap_b - b)),  # Pour A → B
            (a + min(b, cap_a - a), b - min(b, cap_a - a))   # Pour B → A
        ]

        for move in moves:
            if move not in visited:
                queue.append((move, path))

    return None


# Run the solution
solution = water_jug_problem()

if solution:
    print("Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")