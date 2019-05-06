class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        newS = []
        roman = ["I","V", "X","L","C","D","M"]
        romanBig = [["I", 1],["V", 5],["X", 10],["L", 50],["C", 100],["D",500],["M",1000]]
        j = 0
        for i in range (0, len(s)):
            if i > 0:
                if romanBig[roman.index(s[i - 1])][1] < romanBig[roman.index(s[i])][1]:
                    newS[j-1] = "0"
                    newS.append(str(romanBig[roman.index(s[i])][1] - romanBig[roman.index(s[i-1])][1]))
                else:
                    newS.append(str(romanBig[roman.index(s[i])][1]))
            else:
                newS.append(str(romanBig[roman.index(s[i])][1]))
            j += 1
        total = 0
        for i in newS:
            total += int(i)
        return total