class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in S:
            for j in J:
                if i == j:
                    count += 1
        return count