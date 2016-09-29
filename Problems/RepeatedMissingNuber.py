# @param A : tuple of integers
# @return a list of integers
def repeatedNumber( A):
    S = sum(A)
    for i in range(0,len(A)):
        number = A[i]
        targetIndex = number-1
        while (A[targetIndex]>0):
            temp = A[targetIndex]
            A[targetIndex]=-1*A[targetIndex]
            targetIndex = temp-1
    for i in range(0,len(A)):
        if A[i]>0:
            missingNumber = i+1
    SumN = (len(A)*(len(A)+1))/2
    repeatedNum = S - SumN +missingNumber
    return [repeatedNum,missingNumber]


def repeatedNumberNoSpace(A):
    S = sum(A)
    n = len(A)
    SumSquaredA = sum([x**2 for x in A])
    SumSquaredN = (n*(n+1)*((2*n)+1))/6
    SumN = (n*(n+1))/2
    d = S - SumN
    r = (d**2 + SumSquaredA - SumSquaredN)/(2*d)
    m = r - d
    return [r,m]

def repeatedNumberAnother(A):
    for number in A:
        target = abs(number) -1
        while (A[target] > 0 ):
            A[target] = -A[target]
            target = abs(A[target])-1
    for i in range(len(A)):
        if A[i]>0:
            return i+1
    return -1

print repeatedNumberAnother([1,2,3,4,4])
#Think without using extra space
#The array is read-only too.
'''
    for every number:
        target index = number-1
        see if it is negative (stop)
        else:
            while (a[targeIndex]<0)
            save if it positive
            make the target blah negative
            change targetindex
    find the one positive number

    [1 .r r.. n ] +m -m =S
    [1 .. r .m ..n] -m +r = S
    -m + r + n(n+1)/2 = S
    r -m = S -n(n+1)/2
    r - m r+m = SumSq
    r + m = SumSq/d
     [sum of squares ]  + m2 -m2 = SumSq

'''
