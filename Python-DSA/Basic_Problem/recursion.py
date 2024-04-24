# recursion : function call itself

# why we use recursion?
# it helps to solve bigger or complex problem in simple way
# we can convert recrusion solution into iteration(loop) and vice-versa

# space complexity is not constant because of function calls

# fibonacci number

# 0 1 1 2 3 5 8 13 ..

# fibo(n) = fibo(n-1) + fibo(n-2)   (recurrence relation)
#               | 
#           fibo(n-1) = fibo(n-2) + fibo(n-3)

# base condition of fibo = fibo(0)-->0, fibo(1)-->1

# last function call is known as tail recursion


def fibo(n):
    # base condition
    if(n<2): 
        return n

    return fibo(n-1) + fibo(n-2)

# print(fibo(6))

# binary search

# binarySearch(n) = O(1) {comparison} + binarySearch(n/2) {dividing in half}

# types of recurrence relation 
# linear  (like fibonacci)
# divide and conqure (like binary search)


# notice here at variable
# which is passed in function argument
# which is passed in function body
# what is the return type of function


def binary(arr, target, start, end):
    # target not find
    if(start > end):   # this is also base condition
        return -1
    
    mid = (start + end) // 2

    if (arr[mid] == target):   # base condition
        return mid
    
    if (target < arr[mid]):
        # left search (end will update)
        return binary(arr, target, start, mid - 1)
    
    # right search  (start will update)
    return binary(arr, target, mid + 1, end)


arr = [3,4,33,45,88, 101,199]
result = binary(arr, 1, 0, len(arr))
print(result)