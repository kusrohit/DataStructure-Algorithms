# Problem

# 0! = 1
# 1! = 1
# 2! = 1*2 = 2
# 3! = 1*2*3 = 6
# 4! = 1*2*3*4 = 24
# 5! = 1*2*3*4*5 = 120

# algo

# fact = 1
# i=1
# for i to n:
#     fact = fact * i



def factorial(input: int) -> int:
    fact = 1
    for i in range(1,input+1):
        fact *= i
    return fact

def main():
    # test cases

    print(factorial(2))
    print(factorial(5))
    print(factorial(10))


if __name__ == "__main__":

    main()