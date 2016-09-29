class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(0,len(nums)):
            a = nums[i]
            s = -a
            hm = set()
            #find two numbers in array that sum to s
            for j in range(0,len(nums)):
                if j!=i:
                    if (s-nums[j]) in hm:
                        res.append([a,nums[j],s-nums[j]])
                    hm.add(nums[j])
        return res


s = Solution()
s.threeSum([-1,0,13,4])