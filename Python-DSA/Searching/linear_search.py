# linear search
# 
# 1. go through every element
# 2. check if no is match with search element
# if found return true
# 
#  
# import numpy as np

# 
# general code
# 
# def linear_search(arr, n, x):
#   for i in range(0,n):
#     if(x == arr[i]):
#       print(f'search element: {x}, found at arr[{i}]: {arr[i]}')
#     # print(f'arr[{i}]: {arr[i]}')
#   return True


# 
# optimize code
# 

# def linear_search(arr, n, x):
#   for i in range(0, n):
#     if (x == arr[i]):
#       print(f'search element: {x}, found at arr[{i}]: {arr[i]}')
#       return True


# def arr_generate():
#   arr = np.random.randint(0,100000000,100000000)
#   return arr


# def main():
#   # arr = [23,45,22,19,21,50,5,24,33]
#   arr = arr_generate()
#   size = len(arr)
#   search_element = 5

#   # testing
#   # linear_search(arr, size, search_element)

#   is_found = linear_search(arr, size, search_element)
#   print("Search element: ", search_element)
#   print('No is found: ', is_found)

# if __name__ == "__main__":
#   main()



# def linear_search(arr, target):
    
#     # if arr is empty
#     if len(arr) == 0:
#         return
    
#     # if arr has element
#     for i in range(len(arr)):
#         if target == arr[i]:
#             return i, arr[i]
        
#     # if target is not found
#     return


# def linear_search_sub_part(arr, target, start, end):
    
#     # if arr is empty
#     if len(arr) == 0:
#         return
    
#     # if arr has element
#     for i in range(start,end):
#         if target == arr[i]:
#             return i, arr[i]
        
#     # if target is not found
#     return


# def min_search(arr):
    
#     # if arr is empty
#     if len(arr) == 0:
#         return
    
#     # if arr has element
#     min = arr[0]
#     for i in range(len(arr)):
#         if min < arr[i]:
#             min = arr[i]
#     return i, arr[i]


def searchIn2dArray(arr, target):
    
    # if arr is empty
    if len(arr) == 0:
        return
    
    # if arr has element
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if target == arr[row][col]:
                return row, col, arr[row][col]




arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
target = 5
# start = 8
# end = 17


result = searchIn2dArray(arr, target)
if result:
    row, col, element = result
    print(f'Element {element} found at position ({row}, {col})')
else:
    print('Element not found')
    