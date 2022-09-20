# // Evaluate with Loops
# Input = List of coefficients, and value of x in term
# Result = 0
# Start = start time
# For counter in List Size
# 	Result = Result + List[counter] * x^(len(list)-counter)
# Stop = stop time
# Runtime = Stop – Start
# Return Result, Runtime

# // Evaluate with Horner’s Method
# 1.	Input = List of coefficients, and value of x in term
# 2.	Initialize the value of the result to the coefficient of the first term or index
# a.	Result = List[0]
# 3.	Start = start time
# 4.	For counter in range(1, len(list))
# a.	Result = Result * x + List[counter]
# 5.	Stop = stop time
# 6.	Runtime = Stop – Start
# 7.	Return Result, Runtime


import time, random

def main():
    # Generate a random list of size n
    coefficients = randomList(3)
    
    start = time.time()
    output = evaluatePoly(coefficients, 1.5)
    stop = time.time()
    runtime = stop -  start

    print(f"Evaluation method Output: {output}")
    print(f"Runtime: {runtime}")

    print()

    start = time.time()
    output = horner(coefficients, 1.5)
    stop = time.time()
    runtime = stop -  start

    print(f"Horner's method Output: {output}")
    print(f"Runtime: {runtime}")

    return
    

# Evaluate with Loops
# P(x) = Sum of evaluating each element of coefficient list,
# Multiplying each coefficient with the constant x^n-1
# Summing the result with next coefficient...

def evaluatePoly(list, x):
    result = 0
    print("Loops through list and evaluate polynomial")
    for index, value in enumerate(list, start = 1):
        result = result + value*(x**(len(list)-index))
        print(f"index: {index}, value={value}")
    return result



# returns value using Horner's method
def horner(list, x):

    # initialize result value
    result = list[0]

    print("Evaluate polynomial using Horner's method")
    for i in range(1, len(list)):
        result = result * x + list[i]
        print(f"index: {i}, value: {list[i]}")
    return result


# Generate a random list of n vectors with non-negative elements
def randomList(n):
    v = []
    randomNumber = 0
    
    for i in range(n):
        randomNumber = random.randint(1,5)
        v.append(randomNumber)
    
    return v


main()

