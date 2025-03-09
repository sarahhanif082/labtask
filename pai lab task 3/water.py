def dfs_water_jug(capacity1, capacity2, goal):
    stack = []
    visited = set()

    stack.append((0, 0)) 
    visited.add((0, 0))

    actions = []

    while stack:
        jug1, jug2 = stack.pop()
        actions.append((jug1, jug2))
        if jug1 == goal or jug2 == goal:
            print("\n✅ Solution Found using DFS:")
            for action in actions:
                print(action)
            return True

        
        possible_moves = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),  
            (jug1, 0),  
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1)),  
        ]

        for state in possible_moves:
            if state not in visited:
                visited.add(state)
                stack.append(state)

    print("\n No Solution found using DFS")
    return False


jug1Capacity = 4
jug2Capacity = 3
target = 2


dfs_water_jug(jug1Capacity, jug2Capacity, target)
