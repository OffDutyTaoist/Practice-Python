def find_min(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest 

print(find_min([1, 2, 3, -1, 6, -3]))
