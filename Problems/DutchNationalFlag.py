class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums)-1
        m = (low+high)/2
        while(m<=high):
            if nums[m] == 0:
                nums[m],nums[low] = nums[low],nums[m]
                m += 1
                low += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[high],nums[m] = nums[m],nums[high]
                high -= 1
            m = (low+high)/2
        return
sol = Solution()
sol.sortColors([0,0,0,2,2,1,2,1,0,0,2])