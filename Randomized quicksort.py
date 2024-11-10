import random
import time
# Function to perform the partition
def partition(arr, low, high):
    pivot = arr[high]  # Pivot is chosen as the last element
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

# Randomized Partition (pivot chosen randomly)
def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    return partition(arr, low, high)

# Randomized Quicksort
def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)
# Deterministic Quicksort using the first element as pivot
def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


# Test the function
arr = [12, 7, 14, 9, 10, 11]
randomized_quicksort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr, 0, len(arr) - 1)
    return time.time() - start_time

# Example usage
arr = [random.randint(0, 1000) for _ in range(1000)]
print("Time for randomized quicksort:", measure_time(randomized_quicksort, arr[:]))
print("Time for deterministic quicksort:", measure_time(deterministic_quicksort, arr[:]))
