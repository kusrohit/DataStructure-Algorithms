# optimize way for 2d binary search

# time complexity: O(log n + log m)

# search in the row provided between the col provided
def binarySearch(matrix, row, cStart, cEnd, target):
    while(cStart <= cEnd):
        mid = (cStart + cEnd) // 2

        if(matrix[row][mid] == target):
            return [row, mid]
        
        if(matrix[row][mid] < target):
            cStart = mid + 1
        else:
            cEnd = mid - 1
    
    return [-1, -1]


def search(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])    # be cautious, matrix may be empty

    if (rows == 1):
        return binarySearch(matrix, 0, 0, cols-1, target)

    rStart = 0
    rEnd = rows - 1
    cMid = cols // 2 

    # run the loop till we decreses the row according to target
    #  (reduce the search space)
    while(rStart < rEnd -1):   
        # this narrow down the search space
        #  until a range of element is remain when using <rStart < rEnd>
        #  this narrow down the space and reach at the single element 
        # (check while debugging) and if we not use <rStart < rEnd -1> 
        # it get stuck in infinite loop
        rMid = (rStart + rEnd) // 2

        if(matrix[rMid][cMid] == target):
            return [rMid,cMid]
        
        if(matrix[rMid][cMid] < target):
            rStart = rMid    # we can use rMid+1 becoz mid row has element
        else:
            rEnd = rMid     # we can use rMid-1 becoz mid row has element

    # now we have some rows left
    # check whether the target is in the col of remaining rows

    # search in middle col first element
    if(matrix[rStart][cMid] == target):
        return [rStart, cMid]
    
    # search in middle col but next elemnt
    if(matrix[rStart+1][cMid] == target):
        return [rStart+1, cMid]


    # search in 1st half
    if(target <= matrix[rStart][cMid-1]):
        return binarySearch(matrix, rStart, 0, cMid-1, target)

    # search in 2nd half
    if(target >= matrix[rStart][cMid+1] and target <= matrix[rStart][cols-1]):
        return binarySearch(matrix, rStart, cMid+1, cols-1, target)

    # search in 3rd half
    if(target <= matrix[rStart+1][cMid-1]):
        return binarySearch(matrix, rStart+1, 0, cMid-1, target)

    # search in 4th half
    else:
        return binarySearch(matrix, rStart+1, cMid+1, cols-1, target)



matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print(search(matrix, 15))