# striding

count = 10
numbers = [number for number in range(0, count + 1)]

# format [start: end: step-count]
print("Even numbers", numbers[0: len(numbers): 2])

# The list can be printed backwards by striding
print("Backward iteration", numbers[:: -1])