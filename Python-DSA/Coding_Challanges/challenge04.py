# Ceiling of a number (upper most)

# arr = [2,3,5,6,9,13,16,18]

# ceiling means find the smallest element which is equal or greater then target

# ceiling(arr, target=10) = 13
# ceiling(arr, target=16) = 16

def ceiling_binary_search(arr, target):
    start = 0
    end = len(arr)-1

    if (len(arr) == 0):
        return -1
    

    if (target > arr[end]):
        return -1
    
    while(start <= end):
        mid = (start + end) // 2

        if(target < arr[mid]):
            end = mid -1
        elif(target > arr[mid]):
            start = mid +1
        else:
            return mid

    return start

arr = [23,24,26,45,48,56,67,99,101,123]
# arr = []
target = 124

print(ceiling_binary_search(arr, target))

