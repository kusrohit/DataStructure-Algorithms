
# Lomuto partition (fastest way to sorting)
# enhance quick sorting

# Time complextity : O(n^2)
# Space complextity : O(1)


def partition(arr, low, high):

    # node
    node = arr[high]

    i = (low -1)
    for j in range(low, high):

        if arr[j] <= node:
            i += 1

            arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)

def quichSort(arr, low, high):
    if(low < high):
        pi = partition(arr, low, high)
        quichSort(arr, low, pi-1)
        quichSort(arr, pi+1, high)


def printArray(arr, size):
    
    for i in range(size):
        print(arr[i], end=" ")

    print()



# driver code
def main():
    arr = [10,2,30,4,0,0.5,1,3,4,9]
    size = len(arr)
    quichSort(arr,0, size-1)

    print(f'Sorted Arrary : ')
    printArray(arr, size)

if __name__ == "__main__":
    main()