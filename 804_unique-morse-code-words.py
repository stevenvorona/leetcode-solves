class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        mapped = dict(zip(letters, morseCode))
        morseList = [];
        morse = ""
        for i in words:
            for j in i:
                morse += mapped[j]
            morseList.append(morse)
            morse = ""
        morseListFinal = [];
        for i in morseList:
            if (i not in morseListFinal):
                morseListFinal.append(i)
        return len(morseListFinal)