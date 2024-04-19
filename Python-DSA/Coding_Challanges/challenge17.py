# find all the duplicate number

def duplicateNums(arr):
    # 1 to n

    duplicate = []
    i = 0
    while(i < len(arr)):

        correctIndex = arr[i] - 1

        if(arr[i] != arr[correctIndex]):
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]

        else:
            i += 1

    for i in range(len(arr)):
        if(arr[i] != i+1):
           duplicate.append(arr[i])

    return duplicate


arr = [1,1,1,1,1,2,3,4,4,5,6,7]
result = duplicateNums(arr)

print(arr)
print(result)