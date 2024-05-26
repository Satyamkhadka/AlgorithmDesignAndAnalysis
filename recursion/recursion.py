# a simple recursive function to print number from 1 to n

def print_num_one_to_n(n):
    if n==0: # this is the base case or stopping rule
        return
    print_num_one_to_n(n-1)
    print(n) # here number gets printed
    
print_num_one_to_n(10) # called from here. It should print from 1 to 10

# another example of a recursive function to print from n to 1

def print_num_n_to_one(n):
    if n==0:
        return
    print(n)
    print_num_n_to_one(n-1)

print_num_n_to_one(10)

# If we see second example, the difference is that it prints from 10 to 1
# this is because print operation is called before the recursion call 
# hence, the operation is done when the execution stack is being made 
# but in the example above the operation is done when the recursion stack is being cleared after reaching the base case or termination case
