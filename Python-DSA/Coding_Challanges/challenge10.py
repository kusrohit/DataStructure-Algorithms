# find element in rotated binary search






def rotatedBinarySearch():
    arr = [4,5,6,0,1,2,3]
    target = 3
    # print(findPivot(arr)) 

    pivot = findPivot(arr)

    # if we did'nt find pivot
    if(pivot == -1):
        # just do normal binary search
        return binarySearch(arr, target, 0, len(arr)-1)
    
    # if pivot is found, we have 2 asc sorted array
    if(arr[pivot] == target):
        return pivot
    
    # if target > start then search space decrease to start till pivot-1
    if(target >= arr[0]):
        return binarySearch(arr, target, 0, pivot -1)
    
    # if target < start then search space decrease to pivot+1 till end
    return binarySearch(arr, target, pivot+1, len(arr)-1)


def binarySearch(arr, target, start, end):
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
    return -1

        


def findPivot(arr):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = (start + end) // 2

        # case 1
        if(arr[mid] < arr[mid - 1]):
            # pivot
            return mid - 1
        
        # case 2
        if(mid < end and arr[mid] > arr[mid + 1]):
            # pivot
            return mid
        
        # case 3
        if(arr[mid] <= arr[start]):
            end = mid -1
        # case 4
        else:
            start = mid + 1

    return -1


print(rotatedBinarySearch())   