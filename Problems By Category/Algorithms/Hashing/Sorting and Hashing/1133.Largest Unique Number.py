def LargestUniqueNumber(nums):
    unique = set()
    repeated = set()
    for num in nums:
        if num in unique:
            unique.remove(num)
            repeated.add(num)
        unique.add(num)
    return max(unique) if unique else -1
