import functools
def mycmp(s1,s2):
    if len(s1)!=len(s2) and (s2.find(s1)!=0 or s1.find(s2)!=0):
        return cmp(s1+s2,s2+s1)
    else:
        return cmp(s1,s2)


    # @param A : tuple of integers
    # @return a strings
    # 2:52
    #[3, 30, 34, 5, 9]
    #Ret : 9534330
    #sorted = ['9', '5', '34', '3', '30']
    # 30 3 34 5 9
    # 30 3
    # if 30 + 3  3 + 30
def largestNumber(A):
    A = sorted(map(str, A), key=functools.cmp_to_key(mycmp),reverse=True )
    allZeros=all([x=='0' for x in A ])
    return '0' if allZeros==True else ''.join(A)
print largestNumber([0,0])

