# Bubble sort
# Logic: It compares two adjacent(nearby) element in every pass

# Best case: O(n) { if the element is in ascending order}
# Worst case: O(n^2) { if the element is in descending order}

# def bubble_sort(arr):

#     flag = False

#     for i in range(len(arr)-1):
#         print("Pass: ", i+1)
#         for j in range(len(arr)-i-1):
#             if(arr[j]>arr[j+1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#                 flag = True

#                 print(arr, "Swapped", arr[j], arr[j+1]) # swapped iteration
#             else:
#                 print(arr, "not swapped", arr[j], arr[j+1]) # not swapped iteration
#         print()
#         if (flag == False):
#             return arr;
#     print('Reached')
#     return arr


# def main():
#     # arr = [34,23,2,44,1,0,9]
#     arr = [1,2,3,4,5,6,0]
#     print('Unsorted Array: ', arr)

#     result = bubble_sort(arr)
#     print('Sorted Array: ', result)


# if __name__ == "__main__" :
#     main()


def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            # swap
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]



arr = [1, -2, 3, 4, 5, 6, -9, 8]

bubblesort(arr)
print(arr)

