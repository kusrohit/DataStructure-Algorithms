# Problem statement

# 0,1,1,2,3,5,8,13,....

# algo

# n = how many digit
# a,b = 0,1
# for 0 to n-2:
#     next = a + b
#     a = b
#     b = next
#     print (next)
#




# n = upto that
      

def fibo_pattern(n:int) -> None:
    first, second = 0,1
    while first <= n:
        print(first, end=",")
        next = first + second
        first = second
        second = next



# n = how many number

# def fibo_pattern(n:int) -> None:

#     first, second = 0,1
#     for _ in range(n):
#         print(first, end=",")
#         next = first + second
#         first = second
#         second = next


# def fibo_pattern(n:int) -> None:

#     if n<3:
#         print(f'fibo pattern for input: {n}')
#         return
#     else:
#         print(f'fibo pattern for input: {n}')

#     first, second = 0,1
#     print(first,second, end=",")
    
#     for i in range(n-2):
#         next = first + second
#         first = second
#         second = next
#         print(next,end=",")
#     print()


def main():

    # test cases
    # fibo_pattern(1)
    fibo_pattern(10)
    fibo_pattern(100)



if __name__ == "__main__":
    main()