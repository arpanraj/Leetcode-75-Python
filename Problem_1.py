class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = len(word1)
        l2 = len(word2)
        min_l = min(l1, l2)
        combined = ""
        for i in range(min_l):
            combined += word1[i] + word2[i]
        if l1 > l2:
            return combined + word1[min_l:]
        elif l1 < l2:
            return combined + word2[min_l:]
        return combined
