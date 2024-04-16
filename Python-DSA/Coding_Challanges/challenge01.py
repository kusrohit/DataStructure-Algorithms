# fizzbuzz problem

# takes a number list and add only even number in the list
# then return it 


# def even_sum(num_list):
#   size = len(num_list)
#   sum = 0
#   for i in range(size):
#     if (num_list[i] % 2 == 0):
#       sum += num_list[i]
#   return sum

def even_sum(num_list):
    size = len(num_list)
    sum = 0
    for i in range(size):
        if num_list[i] % 2 == 0:
            sum += num_list[i]
    return sum

# Test cases
def test_even_sum():
    print(even_sum([2, 4, 6, 8]))
    print(even_sum([1, 3, 5, 7]))
    print(even_sum([1, 2, 3, 4, 5, 6]))
    print(even_sum([-2, -4, -6, -8]))
    print(even_sum([]))
    print(even_sum([5]))
    print(even_sum(list(range(1, 10001))))

# Run the test cases
test_even_sum()

