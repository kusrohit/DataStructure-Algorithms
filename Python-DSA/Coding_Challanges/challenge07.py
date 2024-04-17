# find the element in sorted infinite array (here infinite means dont use len() function)


# we are using here bottom up approach

def findRange(arr, target):
    # first find the range

    # we are going to start with arr with size of 2
    start = 0
    end = 1

    # check the target to lie in the range
    while(target > arr[end]):
        newStart = end + 1 
        # double the arr
        # newEnd = (2* len(arr)) + previousEnd
        # len(arr) = end - start + 1
        end = ((end - start + 1) * 2 ) + end

        start = newStart 

    return infiniteArraySearch(arr,target, start, end)



def infiniteArraySearch(arr, target, start, end):
    while(start <= end):
        mid = (start + end) // 2

        if(target < arr[mid]):
            end = mid -1 
        elif(target > arr[mid]):
            start = mid +1
        else:
            # ans found
            return mid
    return -1

arr = [3, 4, 6, 9, 10, 13]

target = 10

print(findRange(arr, target))


# this code needs some modification becaues this gives some out of range error in findRange function 

# NOTICE : this is solve using generator function 