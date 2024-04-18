# find element in rotated binary search with duplicate value






def rotatedBinarySearch():
    arr = [4,5,6,0,1,2,3]
    target = 3
    # print(findPivot(arr)) 

    pivot = findPivotWithDuplicate(arr)

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

        


def findPivotWithDuplicate(arr):
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
        # if element at mid, start and end are equal than just skip the duplicate
        if(arr[mid] == arr[start] and arr[mid] == arr[end]):
            # skip the duplicate
            # note: what if the start and end are pivot

            # check if start is pivot
            if(arr[start]> arr[start+1]):
                return start
            start += 1
            
            # check whether end is pivot
            if(arr[end] < arr[end -1]):
                return end-1
            end -= 1

        # left side is sorted, so pivot should be in right
        elif(arr[start] < arr[mid] or arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid+1
        else:
            end = mid-1
            

    return -1


print(rotatedBinarySearch())   