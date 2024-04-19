# missing multiple nums

# input = [4,3,2,7,8,2,3,1]


def missingMultiElement(arr):
    missingElement = []
    i = 0
    while(i < len(arr)):
        correctIndex = arr[i] -1

        if(arr[i] != arr[correctIndex]):
          arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
        else:
           i += 1

        
    # misssing element

    for i in range(len(arr)):
        if(arr[i] != i+1):
           missingElement.append(i+1)

    return missingElement

arr = [4,3,2,7,8,2,3,1]
result = missingMultiElement(arr)
print(result)        
print(arr)