def firstMissingPositive(A):
    hm = [0 for _ in range(len(A)+1)]
    for num in A:
        if 1<=num<=len(A):
            hm[num]=1
    for i in range(1,len(A)+1):
        if (hm[i]==0):
            return i
    return (len(A)+1)
print firstMissingPositive([1])