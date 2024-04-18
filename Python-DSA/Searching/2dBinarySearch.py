# Binary search in 2d

# time complexity = row+col = n + n = 2n = O(n)


# linear search

# def linearSearch2d(arr, target):
#     for row in range(len(arr)):
#         for col in range(len(arr[row])):
#             if(target == arr[row][col]):
#                 return row,col
            

# arr = [[1,2,3],[32,2,45],[23,45,56],[0,11,32]]
# target = 0

# row, col = linearSearch2d(arr, target)
# print(row, col)



# general concept like linear

def binarySearch2d(matrix, target):
    row = 0    # start
    # col = len(matrix) - 1    # end for n*n matrix
    col = len(matrix[row]) - 1    # end for n*m matrix this works for N*N also

    # why: because row is increasing and col is decrease to reduce the search space
    while(row < len(matrix) and col >= 0):
        if(matrix[row][col] == target):
            return [row, col]
        
        if(matrix[row][col] < target):
            row += 1

        else:
            col -= 1

    return [-1,-1]

matrix = [[10,20,30,40],[15,25,35,45],[28,29,37,49],[33,34,38,50]]
target = 34
print(binarySearch2d(matrix, target))

