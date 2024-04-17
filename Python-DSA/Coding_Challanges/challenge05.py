# Smallest letter greater than target

# arr = ['c', 'd', 'g', 'j']
# target = 'e'
# output = 'g'

# also wrap aroud means if target is not found return the 0th index element

# here we not considering equal to the target

# here ceiling concept applied
# ceiling means find the smallest element which is equal or greater then target

# ceiling(arr, target=10) = 13
# ceiling(arr, target=16) = 16

def smallestChar(letters, target):
    start = 0
    end = len(letters)-1

    if (len(letters) == 0):
        return -1

    while(start <= end):
        mid = (start + end) // 2

        if(target < letters[mid]):
            end = mid -1
        else:
            start = mid +1
        

    return letters[start % len(letters)]

    # alternative solution
    # if (start == len(letters)):
    #     return letters[0]

letters = ['c', 'd', 'g', 'j']
target = 'z'

print(smallestChar(letters, target))

