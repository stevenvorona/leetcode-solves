class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        size = len(A[0])
        for j in A:
            for i in range(0, int(size/2)):
                swapFront = j[i]
                swapBack = j[size - i - 1]
                j[i] = swapBack
                j[size - i - 1] = swapFront
        for i in A:
            for j in range(0, len(i)):
                if(i[j]):
                    i[j] = 0
                else:
                    i[j] = 1
        return A