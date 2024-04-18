# find element in Mountain array

# arr [1,2,3,4,5,4,3,1]
# target = 4
# output = 3 (index)

# steps

# 1. find peak
# 2. first try in asscending order
# 3. second try in decending order

def searchInMountain(arr, target):
    peek = peekIndex(arr)

    firstTry = orderAgnosticSearch(arr, target, 0, peek)  # arr, target, start, end

    if(firstTry != -1):
        return firstTry
    
    return orderAgnosticSearch(arr, target, peek+1, len(arr)-1)

def peekIndex(arr):
    start = 0
    end = len(arr) - 1

    while(start < end):
        mid = (start+end)//2

        if(arr[mid] > arr[mid+1]):
            end = mid
        else:
            start = mid + 1

    return start


def orderAgnosticSearch(arr, target, start, end):
    isAscending = arr[start] < arr[end]

    while(start<=end):
        mid = (start + end) // 2

        # don't forget equal case
        if(arr[mid] == target):
            return mid

        if(isAscending):
            if(target < arr[mid]):
                end = mid - 1
            else:
                start = mid + 1
        else:
            if(target < arr[mid]):
                start = mid + 1
            else:
                end = mid - 1
    
    return -1


arr = [1,2,3,4,5,3,2,1]
target = 3

print(searchInMountain(arr, target))

        