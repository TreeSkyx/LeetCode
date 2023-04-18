"""
    1768. Merge Strings Alternately
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
    If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string.

    :type word1: str
    :type word2: str
    :rtype: str

"""
def mergeAlternately(word1, word2):
    ans = ""
    m = max(len(word1),len(word2))
    for i in range(m):
        if i <= (len(word1)-1):
            ans += word1[i]
        if i <= (len(word2)-1):
            ans += word2[i]
    return ans

print(mergeAlternately("ab","pqrs"))