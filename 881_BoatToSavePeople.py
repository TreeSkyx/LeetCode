"""
    881. Boats to Save People
    You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a 
    maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.

    :type people: List[int]
    :type limit: int
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""

def numRescueBoats(people, limit):
    people = sorted(people)
    left, right, boats = 0, len(people) - 1, 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats

print(numRescueBoats([3,5,3,4],5))