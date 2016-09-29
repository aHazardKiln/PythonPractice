# pramp()
# [(a,b)(c,d)()()]




# A[[3,6], [7,8] [9,10]] N  (NlogN)
# B[[1,2],[3,5]  [7,8]]  N   N + N
#sort both of these
# dur = 2
# 1 - > SB
# 2 ->  EB
# 3 -> SA
# 6 _> EA

# left(Tuple1)>right(tuple2) or right(tuple1)<left(tuple2)
#    Do not overlap
# else
#    they overlap
#    max(starts), min(ends)

#sort both
#i, j for A and B
#
def time_available(dur, timesA,timesB):
    timesA = sorted(timesA, key = lambda x : (x[0],x[1]))
    timesB = sorted(timesB, key = lambda x : (x[0],x[1]))
    i = 0
    j = 0
    while ( i < len(timesA) and j < len(timesB)):
        #check if these overlap
        item1 = timesA[i]
        item2 = timesB[j]
        if overlap(item1,item2):
            #calucluate duration and compare
            duration_over = min(item1[1],item2[1]) - max(item1[0],item2[0])
            if duration_over >=dur
                return (max(item1[0],item2[0]),min(item1[1],item2[1]))
        res = compare(item1,item2)
        if res = -1:
            i+=1
        elif res = 1
        j+=1
    else:
        i+=1
        j+=1
return []

def overlap(item1, item2):
    pass

def compare(item1,item2):
    if cmp(item1[0],item2[0])!=0:
        return cmp(item1[0],item2[0])
    else
        return cmp(item1[1],item2[1])