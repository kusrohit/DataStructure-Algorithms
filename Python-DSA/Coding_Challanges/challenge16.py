# find the duplicate number

# input = [1,3,4,2,2]
# output = 2


def duplicateNumber(arr):
    #  1 to n

    i = 0
    while(i < len(arr)):
        # first  we check element is not equal to index+1
        if(arr[i] != i+1):
            correctIndex = arr[i] -1

            # again we check the current element not at correct index
            if(arr[i] != arr[correctIndex]):
                arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
            # else the value is duplicate
            else:
                return arr[i]
        # then go to next index
        else:
            i += 1
        
    return -1


arr = [1,3,4,2,2]
result = duplicateNumber(arr)

print(arr)
print(result)

