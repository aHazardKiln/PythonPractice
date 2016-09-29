class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        if len(A)==0:
            return 0
        #Find left bound
        lb = 0


        #find the right bound
        rb = len(A)-1
        while (rb>=1 and A[rb-1]>=A[rb]):
            rb = rb-1

        rain_area = 0 # 0
        #Execute real logic
        i = 0
        st = []
        while i < rb: #i = 2 lb = 1
            while (lb<rb and A[lb]<=A[lb+1]):
                lb = lb+1
            i = lb+1

            while (i < rb and (len(st)==0 or A[i]<=st[-1])): # 0 < 1
                st.append(A[i]) #0
                i += 1
            h_max = min(A[i],A[lb])

            while (len(st)!=0 and st[-1]<=h_max):
                height_popped = st.pop(-1)
                diff = h_max - height_popped
                if diff > 0:
                    rain_area += diff
                else:
                    break
            #calculate left bound again
            lb = i
            i += 1
        return rain_area

sol = Solution()
A = [ 8, 31, 89, 70, 96, 99, 37, 61, 53, 93, 50, 89, 11 ]
print sol.trap(A)
print str(len(A))+' '+' '.join(map(str, A))