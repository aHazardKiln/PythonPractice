def findPerm(A, B):
    #initialize array
    l = []
    s = [i for i in range(1,B+1)]
    for c in A:
        if c == 'I':
            l.append(s.pop(0))
        if c == 'D':
            l.append(s.pop(-1))
    l.append(s[0])
    return l
print findPerm("IDIDI",6)