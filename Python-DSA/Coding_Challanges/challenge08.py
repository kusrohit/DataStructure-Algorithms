# find the peek element of an array (Mountain or Biotanic array)


# input =    3
#           2  2
#          1    1
#         0      0

# output = 3


# input = [0,1,2,3,2,1,0] output = 3
# input = [1,2,3,,4,2,1]  output = 4

# means find maximum no


def peekIndex(arr):
    start = 0
    end = len(arr) -1

    while(start < end):
        mid = (start + end) // 2

        if(arr[mid] < arr[mid + 1]):
            # we are in ascending order means right side
            # why right: because greater value at right
            # we update start because of right side
            start = mid +1
            # why mid + 1: in cond we check the next value
        else:
            # we are in desecending order means left side
            # why left: because greater value at left
            # we update end value
            # why mid: we check Mid+1
            end = mid
        
    # when condition is break
    # start == end
    return start


arr = [1,2,3,4,9,3,2,1]
print(arr[peekIndex(arr)])