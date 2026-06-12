# Assignment 1
# values = (0, 1, 2)

# if any(values):
  
#   my_var = 0
# # my var will be set to zero because the condition (at least one true value in the tuple named values) is achieved
# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

#   print("Good")
# # This will print Good because the condition (all values from index zero till index 3 must be true) is achieved
# else:

#   print("Bad")
# # The output will be  Good
# Assignment 2
# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820
# # Assignment 3
# n = 20

# l = list(range(n))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#   print("Good")

# # Output => Good
# Assignment 4
def my_all(values):
    for value in list(values):
        if not value:
            return False
        else:
            continue
    return True
# print(my_all(["d", 3, 5, 65, "dkf", "True", False]))
def my_any(values):
    for value in list(values):
        if value:
            return True
        else:
            continue
    return False
# print(any(["", 0, 0, 0, 0, False]))
# print(my_any([0, False, "", "", []]))
def my_max(*nums):
    max = 0
    if len(nums) == 1:
        for num in nums[0]:
            if num > max:
                max = num
    else:  
        for num in nums:
            if num > max:
                max = num
    return max
# print(my_max((3, 5, 9, 10, 19, 20, 34, -1, 100)))
def my_min(*nums):
    min = 0
    if len(nums) == 1:
        for num in nums[0]:
            if num < min:
                min = num
    else:  
        for num in nums:
            if num < min:
                min = num
    return min
# print(my_min([10, 39, 39, 3, -3, 20, -100]))