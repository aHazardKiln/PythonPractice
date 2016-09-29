class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        if len(A)>12 and len(A)<4:
            return []
        return self.restoreIpAddresses1(A,4)

    def restoreIpAddresses1(self,A,size):
        if len(A)<=0 or len(A)>3*size:
            return []
        res = []
        if size==1:
            if self.formsValidSubnet(A):
                res.append(A)
        for i in range(0,3):
            if self.formsValidSubnet(A[0:i+1]):
                comb = self.restoreIpAddresses1(A[i+1:],size-1)
                for s in comb:
                    res.append(A[0:i+1] + "." + s)
        return res

    def formsValidSubnet(self,num):
        if len(num)>len(str(int(num))):
            return False
        if 0<=int(num)<=255:
            return True
        else:
            return False

sol = Solution()
print sol.restoreIpAddresses("0100100")