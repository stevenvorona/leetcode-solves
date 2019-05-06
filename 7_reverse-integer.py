class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """                      
        xStr = str(abs(x))
        reversedInt = int(xStr[::-1])
        if reversedInt > 2147483648:
            return 0
        elif reversedInt == 2147483647 and x < 0:
            return 0
        elif x >= 0:
            return reversedInt
        else:
            return int("-"+str(reversedInt))
            
        