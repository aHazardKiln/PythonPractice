'''
Using normal
 #Does not handle negative case; returns 0 for negative
'''
def maxSubArray1(A):
    local_sum = 0
    max_sum = 0
    for num in A:
        local_sum += num
        max_sum = max(max_sum,local_sum)
        if local_sum<0:
            local_sum=0
    return max_sum

'''
Handles negatives
'''
def maxSubArray2(A):
    local_sum = 0
    max_sum = 0
    for num in A:
        local_sum += num
        if local_sum<0:
            local_sum=0
        elif local_sum>max_sum:
            max_sum=local_sum
    return max_sum
'''Contiguous sum sub-array using dynamic programming'''
def maxSubArray(A):
    max_sum = A[0]
    prev_max=  A[0]
    for i,num in enumerate(A[1:],start=1):
        prev_max = (max(prev_max+A[i],A[i]))
        max_sum=max([max_sum,prev_max])
    return max_sum
print maxSubArray2([-2, -3, -4, -1, -2, -1, -5, -3])