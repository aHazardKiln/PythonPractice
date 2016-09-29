import re
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        inpt = raw_input().strip()
        l = re.split(r'/+',inpt)
        st = []
        for dire in l:
            if dire == "." or dire == "":
                continue
            if dire == "..":
                if len(st)!=0:
                    st.pop(-1)
            else:
                st.append(dir)
        res = "/"
        for dire in st:
            res += dire + "/"
        return res[:-1]
sol = Solution()
print sol.simplifyPath()