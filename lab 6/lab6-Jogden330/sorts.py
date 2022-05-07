import random
import time


def selection_sort(list):
    comps = 0
    for i in range(len(list) - 1):
        min_spot = i
        for j in range(i + 1, len(list)):
            comps += 1
            if list[j] < list[min_spot]:
                min_spot = j
        if i != min_spot:
            swap(list, i, min_spot)
    return comps

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def insertion_sort(alist):
    comparisons = 0
    for i in range(1, len(alist)):
        value = alist[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if value < alist[j]:
                alist[j + 1] = alist[j]
                alist[j] = value
                j = j - 1
            else:
                break
    return comparisons



# Function to do insertion sort


    # Driver code to test above


# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])


# This code is contributed by Mohit Kumra

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 16000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

