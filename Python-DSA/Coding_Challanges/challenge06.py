# Find the first and last index in sorted numsary


# nums = [2,4,5,7,7,7,7,7,8,10,12]
# target = 7
# output = [3,7]


def firstAndLast(nums, target):

    ans = [-1,-1]  # if not found

    # check for first occurence of target
    # start = search(nums, target, True)
    # end = search(nums, target, False)

    # ans[0] = start
    # ans[1] = end

    # alternative

    ans[0] = search(nums, target, True)
    if(ans[0] != -1):
        ans[1] = search(nums, target, False)

    return ans


# returns the index value of target
def search(nums, target, isFind):

    ans = -1
    start = 0
    end = len(nums) -1

    if (len(nums)==0):
        return -1
    
    while(start <= end):
        mid = (start + end) // 2

        if(target < nums[mid]):
            end = mid -1 
        elif(target > nums[mid]):
            start = mid +1
        else:
            # potential ans found
            ans = mid

            if(isFind):
                # we want to seach on left again
                end = mid -1
            else:
                start = mid +1
    return ans


nums = [2,4,5,7,7,7,7,7,8,10,12]
target = 3

print(firstAndLast(nums, target))
