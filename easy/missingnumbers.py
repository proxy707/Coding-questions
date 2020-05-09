class Solution(object):
    def findDisappearedNumbers(self, nums):
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
            print(nums)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

obj=Solution()
obj.findDisappearedNumbers([4,3,2,7,8,2,3,1])