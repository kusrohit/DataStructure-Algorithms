# Two sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# def two_sum(nums: list[int], target: int) -> list[int]:
#     for i in range(len(nums)):
#         # print()
#         for j in range(i+1,len(nums)):
            
#             sum = nums[i] + nums[j]
#             if sum == target:
#                 # print(i,j)
#                 return [i,j]



def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        x = nums[i]
        y = target - x

        for j in range(i+1, len(nums)):
            if y == nums[i+1]:
                # print(i,j)
                return [i]
            

print(two_sum([2,7,11,15], 9))