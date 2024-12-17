def removeElement(self, nums, val):
    temp = []
    for i in range(len(nums)-1):
        if nums[i] == val:
            nums.pop(i)
    return nums
            

print(removeElement("",[0,1,2,2,3,0,4,2],2))