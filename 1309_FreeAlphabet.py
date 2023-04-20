"""
        :type s: str
        :rtype: str
"""

def freqAlphabets(s):
    ans = []
    for i in range(len(s)):
        if s[i] == '#':
            del ans[-2:]
            ans.append(s[i-2:i])
        else:
            ans.append(s[i])
    return ''.join([chr(int(i)+96) for i in ans])

print(freqAlphabets("10#11#12"))