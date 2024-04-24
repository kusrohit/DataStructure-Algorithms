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

print(fibo(6))