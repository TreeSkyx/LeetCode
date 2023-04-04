"""
    496. Next Greater Element I
    The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

    You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

    For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
    If there is no next greater element, then the answer for this query is -1.

    Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def nextGreaterElement(nums1, nums2):
    ans = {}                               
    res = []
    stack = []                              
        
    for n2 in nums2:
        while stack and n2 > stack[-1]:     
            ans[stack.pop()] = n2           
        stack.append(n2)
        
    for n1 in nums1:                        
        res.append(ans.get(n1, -1))         
                                                
    return res

print(nextGreaterElement([4,1,2],[1,2,3,4]))