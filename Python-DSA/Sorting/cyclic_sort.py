# cyclic sort
# when given no from 1 to n use cyclic sort (very imp)
# this works with continuous value from 1 to n

# just like when sorted array use binary search

# it sorts array in single pass(round) we don't use two for loop in this

def cyclicSort(arr):
    i = 0
    while(i < len(arr)):
        correctIndex = arr[i] - 1    # 0th: 3, ka correctIndex = arr[i] - 1 = 3-1 = 2
        if(arr[i] == arr[correctIndex]):
            i += 1
        else:
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]


arr = [5,4,1,2,3,0]   # 1 to n
cyclicSort(arr)

print(arr)