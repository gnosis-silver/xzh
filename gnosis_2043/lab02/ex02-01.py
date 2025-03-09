# Time limit exceeded (3 points)
# If your program runs for more than 3 seconds, please interrupt it manually.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            ###### Your task: Run the code, debug the variable j and update it ######
            j -= 1
        arr[j + 1] = key
    print("Sorted Array:", arr[:5])

arr = list(range(1000, 0, -1))
insertion_sort(arr)


