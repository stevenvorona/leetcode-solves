class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        countR = 0;
        countL = 0;
        countU = 0;
        countD = 0;
        for i in moves:
            if i == 'R':
                countR+=1
            if i == 'L':
                countL+=1
            if i == 'U':
                countU+=1
            if i == 'D':
                countD+=1
        if (countR == countL and countD == countU):
            return True;
        else:
            return False;