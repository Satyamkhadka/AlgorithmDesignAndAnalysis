def min_jumps_recursive(arr,n):
  """
  Finds minimum jumps to reach end of array recursively (exponential time).

  Args:
      arr: The array of jump values.
      n: The length of the array.

  Returns:
      The minimum number of jumps needed, or -1 if unreachable.
  """
  if n == 0:  # Reached end, return 0 jumps
    return 0

  if arr[0] == 0:  # Can't jump from 0, unreachable
    return -1

  # Try all possible jumps from current index
  min_jumps = float('inf')
  for i in range(1, min(arr[0], n) + 1):
    next_jump = min_jumps_recursive(arr[i:], n - i)
    if next_jump != -1:
      min_jumps = min(min_jumps, 1 + next_jump)

  return min_jumps if min_jumps != float('inf') else -1

print(min_jumps_recursive([3,1,3,1,2,9,5,6,7,3,2,9],12))