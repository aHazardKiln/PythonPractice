'''Find the element that occurs more than n/3 times in an array
'''
def repeatedNumber(A):
    d = {}
    for num in A:
        if num in d:
            d[num] += 1
        else:
            if len(d)>2:
                #remove the numbeer with least count
                for (k,v) in d.items():
                    if (v-1)==0:
                        del d[k]
                        d[num]=1
                    else:
                        d[k]=v-1
            else:
                d[num]=1
    for (K,V) in d.items():
        d[K]=0
    for num in A:
        if num in d:
            d[num]+=1
            if d[num]>len(A)/3:
                return num
    return -1
print repeatedNumber([34,34,56])