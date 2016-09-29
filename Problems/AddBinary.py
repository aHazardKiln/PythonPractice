class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        #make the lengths equal
        max_len = max(len(A),len(B))
        A = self.makeLength(A,max_len)
        B = self.makeLength(B,max_len)
        res = ""
        carry = "0"
        #add
        for i in range(len(A)-1,-1,-1):
            res = self.add(carry,self.add(A[i],B[i])) + res
            carry = self.carry(carry,A[i],B[i])
        if carry=="1":
            res = carry + res
        return res

    def makeLength(self,A,d_len):
        if len(A)==d_len:
            return A
        else:
            num_zeroes = d_len-len(A)
            for i in range(0,num_zeroes):
                A = "0"+A
        return A

    def add(self,a,b):
        if a==b:
            return '0'
        else:
            return '1'
    def carry(self,a,b,c):
        if (a=="1" and b == "1") or (b=="1" and c =="1") or (c == "1" and a == "1"):
            return "1"
        else:
            return "0"

sol = Solution()
print sol.addBinary("1","1")