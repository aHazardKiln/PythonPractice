def diagonal(A):
    res = []
    for diag in range(0,len(A)):
        l = []
        startx=0
        starty=diag
        while(startx!=diag+1 and starty!=-1):
            l.append(A[startx][starty])
            startx+=1
            starty-=1
        res.append(l)
    for diag in range(len(A)-2,-1,-1):
        l = []
        startx=diag
        starty=len(A)-1
        while(startx!=len(A) and starty!=diag-1):
            l.append(A[startx][starty])
            startx+=1
            starty-=1
        res.append(l)
    return res
