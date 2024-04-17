# floor of a number (upper most)

# arr = [2,3,5,6,9,13,16,18]

# floor means find the greatest element which is equal or smaller then target

# floor(arr, target=10) = 9
# floor(arr, target=16) = 16

def floor_binary_search(arr, target):
    start = 0
    end = len(arr)-1

    if (len(arr) == 0):
        return -1
    

    while(start <= end):
        mid = (start + end) // 2

        if(target < arr[mid]):
            end = mid -1
        elif(target > arr[mid]):
            start = mid +1
        else:
            return mid

    return end

arr = [23,24,26,45,48,56,67,99,101,123]
# arr = []
target = 1

print(floor_binary_search(arr, target))

