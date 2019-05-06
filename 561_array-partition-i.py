class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum = 0
        length = len(nums)
        for i in range(0, length, 2):
            sum += nums[i]
        return sum
            