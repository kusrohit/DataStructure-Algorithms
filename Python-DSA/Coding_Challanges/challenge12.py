# find the rotation count

def rotationCount():

    arr = [0,1,2,3,4]
    pivot = findPivot(arr)
    
    print(f'rotation count: {pivot+1}')

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


rotationCount()