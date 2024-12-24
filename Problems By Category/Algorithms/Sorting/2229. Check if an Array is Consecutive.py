def isConsecutive(nums):
    if not nums:
        return False
    nums.sort()  
    n = len(nums)
    for i in range(1,n):
        if nums[i] - nums[i - 1] != 1:
            return False
    
    return True
