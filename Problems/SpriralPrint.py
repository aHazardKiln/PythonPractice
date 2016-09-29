def generateMatrix(A):
    toprow = 0
    bottomrow = A-1
    leftcol = 0
    rightcol = A-1
    #initialize the matrix
    m = [[0 for _ in range(A)] for _ in range(A) ]
    value = 1
    while (toprow<=bottomrow and leftcol <= rightcol):
        for i in range(leftcol,rightcol+1):
            m[toprow][i]=value
            value+=1
        toprow+=1
        for i in range(toprow,bottomrow+1):
            m[i][rightcol]=value
            value+=1
        rightcol-=1
        if toprow<=bottomrow:
            for i in range(rightcol,leftcol-1,-1):
                m[bottomrow][i]=value
                value+=1
            bottomrow-=1
        if leftcol<=rightcol:
            for i in range(bottomrow,toprow-1,-1):
                m[i][leftcol]=value
                value+=1
            leftcol+=1
    return m
print generateMatrix(2)