class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xBin = str(bin(x))[2:]
        yBin = str(bin(y))[2:]
        xBinNew = ""
        yBinNew = ""
        if len(xBin) >= len(yBin):
          xBinNew = xBin
          for i in range (0, len(xBin) - len(yBin)):
            yBinNew += str("0")
          yBinNew += yBin
        else:
          yBinNew = yBin
          for i in range (0, len(yBin) - len(xBin)):
            xBinNew += str("0")
          xBinNew += xBin
        bad = 0
        for i in range (0, len(xBinNew)):
          if xBinNew[i] != yBinNew[i]:
            bad += 1
        return (bad)
                