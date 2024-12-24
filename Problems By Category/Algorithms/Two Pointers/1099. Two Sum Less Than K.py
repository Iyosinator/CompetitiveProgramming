def TwoSumLessthanK(nums,k):
    nums.sort()
    left = 0
    right = len(nums) -1
    max_sum = -1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < k:
            left += 1
            max_sum = max(max_sum,current_sum)
        else:
            right-=1
    return max_sum


