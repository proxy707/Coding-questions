def findPairs(self, nums, k):
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res

print(findPairs([3, 1, 4, 1, 5]))