# selection sort

# Best case: O(n^2)
# Worst case: O(n^2)

# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_ptr = i
#         # print(f"Pass : {i}")

#         for j in range(i+1, len(arr)):
#             # print(f"iteration : {j}")
#             if(arr[j] < arr[min_ptr]):
#                 min_ptr = j
            
#             if(min_ptr != i):
#                 arr[i], arr[min_ptr] = arr[min_ptr], arr[i]
    
#     return arr


# def main():
#     arr = [34,5,23,6,114,65,3]
#     print('hi')
#     result = selection_sort(arr)
#     print(result)

# if __name__ == "__main__":
#     main()


def selectionSort(arr):
    for i in range(len(arr)):
        # find the max item in the remaining arr and swap with correct index
        last = len(arr) - i -1


        maxIndex = getMaxIndex(arr, 0, last)
        
        swap(arr, maxIndex, last)


def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]


def getMaxIndex(arr, start, last):
    max = start
    for start in range(last):
        if(arr[max]< arr[start]):
            max = start
    return max



arr = [4,22,5,7,8,1,23,1,4,67,7,5,4,5,5,6]
selectionSort(arr)
print(arr)