def remove_nonints(nums):
    result = []
    for item in nums:
        if type(item) == int:
            result.append(item)
    return result
