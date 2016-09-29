class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s)==0 or s in wordDict:
            return True

        wb = [False]*(len(s)+1)
        for i in range(len(wb)):
            if wb[i] == False and s[:i] in wordDict:
                wb[i] = True

            if wb[i] is True:
                if i == len(wb):
                    return True

                for j in range(i+1,len(wb)):
                    if wb[j] is False and s[i:j] in wordDict:
                        wb[j] = True
                        if j == len(wb)-1:
                            return True
        return False
sol = Solution()
print sol.wordBreak("aaaaa",["aaaa","aa"])