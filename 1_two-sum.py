class Solution(object):
    def twoSum(self, nums, target):
        used1 = -1
        used2 = -1
        for i in range (0, len(nums)):
            for j in range (i, len(nums)):
                if i != j:
                    if (nums[i]+nums[j] == target):
                        used1 = i
                        used2 = j
        nicenums = [used1, used2]
        return nicenums
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """