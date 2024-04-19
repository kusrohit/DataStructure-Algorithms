# missing number

# input = [4,3,1,0], n = 5
# output = 2

def missingNumber(arr):
    i = 0
    while(i < len(arr)):
        correctIndex = arr[i]
        if(arr[i]<len(arr) and arr[i] != arr[correctIndex]):
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
        else:
            i += 1
    

    
    # missing element
    # case 1
    for i in range(len(arr)):
        if(arr[i] != i):
            return i
        
    # case 2
    return len(arr)

arr = [0,6, 4,3,2, 1]
miss = missingNumber(arr)

print(arr)
print(miss)
