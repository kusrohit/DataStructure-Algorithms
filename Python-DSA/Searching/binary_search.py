# binary search

# """
# find the middle element
# target > mid : 
# search in the right 
# else search in left
# if mid == target
# element found


# time complexity: best case => O(1)
#                 worst case => O(log n)

# """

# when arr is sorted in ascending

# def binary_search(arr, target):
#     start = 0
#     end = len(arr)-1

#     while(start <= end):
#         # middle element
#         # if range exceed then for other languge( start + (end - start)/2)
#         mid = (start+end) // 2

#         # target is less than mid element the left search
#         # start does not change
#         if (target < arr[mid] ):
#             end = mid -1

#         # target is more than mid element the right search
#         # end does not change
#         elif (target > arr[mid]):
#             start = mid +1

        
#         # target  found
#         else:
#             return mid
        
#     return -1

# arr = [2,3,4,5,32,54,67,99]
# target = 0

# result = binary_search(arr, target)
# print(result)


# for both ascending and desending array

# order agnostic search
def binarySearch(arr, target):
    start = 0
    end = len(arr) -1

    isAsscending = arr[start] < arr[end]

    if len(arr) == 0:
        return -1
    
    while(start <= end):
        mid = (start + end) // 2


        if(arr[mid] == target):
            return mid
        

        if(isAsscending):
            if (target < arr[mid] ):
                end = mid -1
            else:
                start = mid +1

        else:
            if (target > arr[mid] ):
                end = mid -1
            else:
                start = mid +1

    return -1


arr = [2,3,4,5,32,54,67,99]
target = 54

result = binarySearch(arr, target)
print(result)