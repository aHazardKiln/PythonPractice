def dNums(A, B):
    S = {}
    res = []
    for i in xrange(0,len(A)-B+1):
        if (i==0):
            #add first three numbers to set
            for j in range(0,B):
                S[A[j]]=S.get(A[j],0)+1
            res.append(len(S))
        else:
            S[A[i-1]]=S.get(A[i-1])-1
            if S[A[i-1]]==0:
                del S[A[i-1]]
            S[A[i+B-1]]=S.get(A[i+B-1],0)+1
            res.append(len(S))
    return res
if __name__=="__main__":
    print dNums([1,2,1,3,4,3],3)