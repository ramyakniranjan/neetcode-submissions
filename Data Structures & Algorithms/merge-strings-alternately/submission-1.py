class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        if len1 > len2:
            maxword = word1
            minword = word2
        else:
            maxword = word2
            minword = word1
        count = 0
        mergedWord = ""
        for i in range(len(minword)):
            count += 1
            mergedWord += word1[i] + word2[i]
        return mergedWord + maxword[count:]

        