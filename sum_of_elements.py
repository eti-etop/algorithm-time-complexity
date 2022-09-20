# F(v) = Sum of elements in V

# // This function takes a list and returns the sum of all elements
# 1.	Input = List of random vectors
# 2.	Sum = 0
# 3.	Start = start time
# 4.	For counter in List Size
# i.	Sum = sum + List[counter]
# 5.	Stop = stop time
# 6.	Runtime = Stop - Start
# 7.	Return Sum, Runtime


import time, random

# Main driver
def main():
    # Generate a random list of size n
    randomList = generateRandomList(100)

    start = time.time()
    output = sum(randomList)
    stop = time.time()
    runTime = stop - start

    print(f"Output: {output}")
    print(f"Runtime: {runTime}")


# This function takes a list and returns the sum of all elements
def sum(list):
    sum = 0
    for v in list:
        sum += v
    return sum


# Generate a random list of n vectors with non-negative elements
def generateRandomList(n):
    v = []
    randomNumber = 0
    
    for i in range(n):
        randomNumber = random.randint(1,5)
        v.append(randomNumber)
    
    return v

# Main driver call
main()