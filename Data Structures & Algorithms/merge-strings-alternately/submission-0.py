class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = ""
        iterator=0
        while(iterator<len(word1) or iterator<len(word2)):
            if(iterator<len(word1)):
                newString+=word1[iterator]
            if(iterator<len(word2)):
                newString+=word2[iterator]
            iterator+=1
        return newString
        