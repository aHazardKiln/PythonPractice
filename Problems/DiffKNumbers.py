'''
Given an array of positive, unique, increasingly sorted numbers A,
e.g. A = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13]. Given a positive value K, e.g. K = 3. Output all pairs in A that differ exactly by K.
'''
def findKDiffPairs(arr,K):
    d = set()
    res = []
    for num in arr:
        # if num+K in d:
        #     res.append((num,num+K))
        if num-K in d:
            res.append((num-K,num))
        d.add(num)
    return res
print findKDiffPairs([1, 2, 3, 5, 6, 8, 9, 11, 12, 13],3)