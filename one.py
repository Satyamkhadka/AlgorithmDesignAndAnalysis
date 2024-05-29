class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

def jobScheduling(jobs):
    # Step 1: Sort jobs by their end times
    jobs.sort(key=lambda x: x.end)
    
    # Step 2: Initialize DP array
    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0].profit
    
    # Step 3: Function to find the last non-conflicting job
    def findLastNonConflicting(jobs, index):
        low, high = 0, index - 1
        while low <= high:
            mid = (low + high) // 2
            if jobs[mid].end <= jobs[index].start:
                if jobs[mid + 1].end <= jobs[index].start:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1
        return -1
    
    # Step 4: Fill the dp array using dynamic programming
    for i in range(1, n):
        incl_prof = jobs[i].profit
        l = findLastNonConflicting(jobs, i)
        if l != -1:
            incl_prof += dp[l]
        
        dp[i] = max(incl_prof, dp[i-1])

    # The answer will be in dp[n-1]
    return dp[n-1]

# Example usage:
jobs = [
    Job(1, 4, 50),
    Job(5, 10, 50),
    Job(6, 10, 100),
    Job(11, 50, 200),
    Job(12, 40, 200),
    Job(45, 50, 50),
    Job(55, 100, 200),
]

print(jobScheduling(jobs))  # Output: 150
