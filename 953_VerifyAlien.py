"""
        :type words: List[str]
        :type order: str
        :rtype: bool
"""
def isAlienSorted(words, order):
    ans = []
    for i in words:
        ans.append([order.index(j) for j in i])
    return ans == sorted(ans)
print(isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))