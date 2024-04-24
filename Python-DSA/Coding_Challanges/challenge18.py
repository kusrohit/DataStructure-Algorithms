# set mismatch

# input = [1,2,2,4]
# output = [2,3]  # [duplicate, missing]

def setMisMatch(arr):
    i = 0
    while(i < len(arr)):
        correctIndex = arr[i] - 1    # 0th: 3, ka correctIndex = arr[i] - 1 = 3-1 = 2
        if(arr[i] == arr[correctIndex]):
            i += 1
        else:
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]

    # search for missing number
    for i in range(len(arr)):
        if(arr[i] != i+1):
            return [arr[i], i+1]
    
    return [-1,-1]


arr = [1,2,2,4]
result = setMisMatch(arr)
print(result)


# output = [2,3]  # [duplicate, missing]
