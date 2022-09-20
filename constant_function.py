#  F(v) = A Constant Function

# // Constant Function that adds two integers
# 1.	Input = integer a, b
# 2.	Start = start time
# 3.	Output = a + b
# 4.	Stop = end time
# 5.	Runtime = Stop - Start
# 6.	Return Output, Runtime


from cProfile import run
import time, random
from turtle import clear

# Main driver
def main():
    # 
    a = 1
    b = 1
    start = time.time()
    output = add(a, b)
    stop = time.time()
    runtime = stop - start
    print(f"Input: {a}, {b}")
    print(f"Output: {output}")
    print(f"Runtime: {runtime}")
    return

# Function that adds two integers
def add(a, b):
    # 
    return a + b


# Generate a random list of n vectors with non-negative elements
def generateRandomList(n):
    v = []
    randomNumber = 0
    
    for i in range(n):
        randomNumber = random.randint(1,5)
        v.append(randomNumber)
    
    return v

# Call to main driver
main()