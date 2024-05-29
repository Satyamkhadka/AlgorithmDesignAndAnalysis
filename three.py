def min_cost_assignment(costs):
    n = len(costs)
    assigned = [False] * n
    return assign_task(costs, assigned, 0)

def assign_task(costs, assigned, person):
    n = len(costs)
    if person == n:
        return 0
    
    min_cost = float('inf')
    
    for task in range(n):
        if not assigned[task]:
            assigned[task] = True
            cost = costs[person][task] + assign_task(costs, assigned, person + 1)
            min_cost = min(min_cost, cost)
            assigned[task] = False
    
    return min_cost

# Example usage
costs = [
    [9,2,7,8],
    [6,4,3,7],
    [5,8,1,8],
    [7,6,9,4]
]
print(min_cost_assignment(costs))  # Output will be the minimum cost
