class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        good = True
        ints = []
        for i in range(left,right+1):
            strI = str(i)
            if "0" not in strI:
                good = True
                for j in strI:
                    if i % int(j) != 0:
                        good = False
                        break;
                if good:
                    ints.append(i)
            
        return ints