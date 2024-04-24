# for i in range(4,-1,-1):
#     print(i)


# def insertion(arr):
#     # first element holds

#     for i in range(1, len(arr)):
#         temp = arr[i]

#         j = i-1
#         while(j>=0 and arr[j]>temp):
#             # shift the value
#             arr[j+1]=arr[j]
#             j -= 1
#         arr[j+1] = temp
#     return arr

# def main():
#     arr = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9]
#     result = insertion(arr)
#     print(result)

# if __name__ == "__main__":
#     main()

# import numpy as np

# def arr_generate():
#   arr = np.random.randint(0,100000000,100000000)
#   return True

# is_complete = arr_generate()
# print(is_complete)



# string are immutable

name = 'rohit'
noun = 'rohit'
print(id(name))
print(id(noun))
name[0] = 'm'
print(name[0])
print(id(name))
print(id(noun))