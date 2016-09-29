class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for n in nums:
            s.add(n)

        glo_count = 1
        for n in nums:
            left = n-1
            right = n+1
            count = 1
            while (left in s):
                s.remove(left)
                left -= 1
                count += 1

            while (right in s):
                s.remove(right)
                right += 1
                count += 1

            glo_count = max(glo_count,count)
        return count
sol = Solution()
print sol.longestConsecutive([100,4,200,1,3,2])