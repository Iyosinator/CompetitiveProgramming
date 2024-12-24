def maxSubArrayLen(nums, k):
    prefix_sums = {0: -1}
    prefix_sum = 0
    max_length = 0
    
    for i, num in enumerate(nums):
        prefix_sum += num 
        if prefix_sum - k in prefix_sums:
            max_length = max(max_length, i - prefix_sums[prefix_sum - k])
        if prefix_sum not in prefix_sums:
            prefix_sums[prefix_sum] = i
    
    return max_length
