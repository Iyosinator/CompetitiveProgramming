class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        totalsum = sum(nums)
        leftsum = 0
        answer = []

        for i in range(n):
            rightsum = totalsum - leftsum - nums[i]
            answer.append(abs(leftsum-rightsum))
            leftsum += nums[i]
        return answer