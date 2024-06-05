def conditional_sum(n):
    num = 0
    sum = 0
    while (num < n):
        # sum = 0
        if (num%3 == 0) or (num%5 == 0):
            sum += num
        num += 1
    return sum

if __name__ == "__main__":
    result = conditional_sum(10)
    print(result)

# this problem is giving time limit exceeded error for bigger input
# to solve this error we use mathematical knowledge