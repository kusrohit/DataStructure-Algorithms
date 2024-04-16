# linear search
# 
# 1. go through every element
# 2. check if no is match with search element
# if found return true
# 
#  
import numpy as np

# 
# general code
# 
# def linear_search(arr, n, x):
#   for i in range(0,n):
#     if(x == arr[i]):
#       print(f'search element: {x}, found at arr[{i}]: {arr[i]}')
#     # print(f'arr[{i}]: {arr[i]}')
#   return True


# 
# optimize code
# 
def linear_search(arr, n, x):
  for i in range(0, n):
    if (x == arr[i]):
      print(f'search element: {x}, found at arr[{i}]: {arr[i]}')
      return True


def arr_generate():
  arr = np.random.randint(0,100000000,100000000)
  return arr


def main():
  # arr = [23,45,22,19,21,50,5,24,33]
  arr = arr_generate()
  size = len(arr)
  search_element = 5

  # testing
  # linear_search(arr, size, search_element)

  is_found = linear_search(arr, size, search_element)
  print("Search element: ", search_element)
  print('No is found: ', is_found)

if __name__ == "__main__":
  main()