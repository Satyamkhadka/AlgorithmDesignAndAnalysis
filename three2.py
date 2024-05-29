def min_cost_assignment(costs):
    n = len(costs)
    assigned = [False] * n
    min_cost, assignments = assign_task(costs, assigned, 0, [])
    print("Assignments:")
    for person, task in assignments:
        print(f"Person {person} -> Task {task}")
    return min_cost

def assign_task(costs, assigned, person, current_assignments):
    n = len(costs)
    if person == n:
        return 0, current_assignments
    
    min_cost = float('inf')
    best_assignment = []
    
    for task in range(n):
        if not assigned[task]:
            assigned[task] = True
            next_assignments = current_assignments + [(person, task)]
            cost, assignments = assign_task(costs, assigned, person + 1, next_assignments)
            total_cost = costs[person][task] + cost
            if total_cost < min_cost:
                min_cost = total_cost
                best_assignment = assignments
            assigned[task] = False
    
    return min_cost, best_assignment

# Example usage
costs = [
    [9,2,7,8],
    [6,4,3,7],
    [5,8,1,8],
    [7,6,9,4]
]
print("Minimum cost:", min_cost_assignment(costs))  # Output will be the minimum cost and the assignments
