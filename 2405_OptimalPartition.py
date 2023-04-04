"""
    2405. Optimal Partition of String
    Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
    That is, no letter appears in a single substring more than once.

    Return the minimum number of substrings in such a partition.

    Note that each character should belong to exactly one substring in a partition.

    :type s: str
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def partitionString(s):
    last_pos = [0] * 26
    partitions = 0
    last_end = 0
    for i in range(len(s)):
        if last_pos[ord(s[i]) - ord('a')] >= last_end:
            partitions += 1
            last_end = i + 1
        last_pos[ord(s[i]) - ord('a')] = i + 1
    return partitions