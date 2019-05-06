class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = ""
        lenPref = 0
        maxlen = 0
        for i in strs:
            if len(i) > maxlen:
                maxlen = len(i)
        shortlen = maxlen
        for i in strs:
            if len(i) < shortlen:
                shortlen = len(i)
        for i in range(0, shortlen):
            cur = (strs[0])[i]
            for j in strs:
                if j[i] != cur:
                    return pref
            pref += cur
        return pref