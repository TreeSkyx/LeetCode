def removeDuplicates(self, nums):
    arr = []
    for i in range(len(nums)):
        if nums[i] not in arr:
            arr.append(nums[i])
    nums[:] = arr
    return len(nums)
    
print(removeDuplicates("", [1,1,2]));
print(removeDuplicates("", [0,0,1,1,2,2,3,3,4]));
