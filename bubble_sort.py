# 5. Bubble Sort of the elements of V

# //By traversing through all list in V
# //And checking if next list is lower
# //If so switch
# 1.	Input = List of non-negative integers
# 2.	Start = start time
# 3.	For i in range(len(List))
# a.	For j in range(0, n-i-1)
# i.	If list[j] > list[j+1]:
# 1.	List[j], list[j+1] = list[j+1], list[j]
# 4.	Stop = stop time
# 5.	Runtime = Stop – Start
# 6.	Return Runtime


import time, random

def main():
    arr = generateRandomList(3200)

    # print("Unsorted array is:")
    # for i in range(len(arr)):
    #     print("%d" % arr[i], end=" ")

    start = time.time()
    bubbleSort(arr)
    stop = time.time()
    runningTime = stop - start
    
    print(f"Runtime: {runningTime}")

    

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
 

# Generate a random list of n vectors with non-negative elements
def generateRandomList(n):
    v = []
    randomNumber = 0
    
    for i in range(n):
        randomNumber = random.randint(1,50)
        v.append(randomNumber)
    
    return v

main()

 
  