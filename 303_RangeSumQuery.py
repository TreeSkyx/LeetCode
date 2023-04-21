class NumArray(object):

    def __init__(self, nums):
        self.sum = []
        sum_till = 0
        for i in nums:
            sum_till += i
            self.sum.append(sum_till)

    def sumRange(self, left, right):
        if left > 0 and right > 0:
            return self.sum[right] - self.sum[left - 1]
        else:
            return self.sum[left or right]
