class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        #Run a DFS on all boundry points
        cols = len(A[0])
        rows = len(A)
        #top row
        for i in range(cols):
            if A[0][i] == 'O':
                self.markInvalid(A,0,i)

        #bottom row
        for i in range(cols):
            if A[len(A)-1][i] == 'O':
                self.markInvalid(A,len(A)-1,i)

        #Right column
        for i in range(rows):
            if A[i][cols-1] == 'O':
                self.markInvalid(A,i,cols-1)

        #Left column
        for i in range(rows):
            if A[i][0] == 'O':
                self.markInvalid(A,i,0)

        self.convert(A,'O','X')
        self.convert(A,'A','O')
        print A

    def markInvalid(self,A,i,j):
        if (0<=i<len(A) and 0<=j<(len(A[0]))) is False:
            return
        if A[i][j]!='O':
            return
        A[i][j]='A'
        self.markInvalid(A,i+1,j)
        self.markInvalid(A,i-1,j)
        self.markInvalid(A,i,j+1)
        self.markInvalid(A,i,j-1)
        return

    def convert(self,A,find,replace):
        rows = len(A)
        cols = len(A[0])
        for i in range(rows):
            for j in range(cols):
                if A[i][j]==find:
                    A[i][j]=replace
        return

sol = Solution()
N = int(raw_input())
M = []
for i in range(N):
    row = raw_input().strip().split()
    M.append(row)
sol.solve(M)