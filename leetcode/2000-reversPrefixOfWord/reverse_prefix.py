class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        if index == -1:
            return word
        else:
            return word[:index+1][::-1] + word[index+1:]
