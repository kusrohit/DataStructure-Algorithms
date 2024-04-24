# first missing positive

# input = [-1,3,1,4]
# output = 2

# input = [7,8,9,10,11]
# output = 1

# ignore element that are -ve number and > n

def positiveMissing(arr):
    i = 0
    while(i < len(arr)):
        correctIndex = arr[i] - 1    # 0th: 3, ka correctIndex = arr[i] - 1 = 3-1 = 2
        if(arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[correctIndex]):
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
        else:
            i += 1

    # search for missing number
    for i in range(len(arr)):
        if(arr[i] != i+1):
            return i+1
    
    return len(arr) + 1

arr = [-1,0,3,2,1,4]
result = positiveMissing(arr)
print(result)
