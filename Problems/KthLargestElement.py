import heapq
def findKthLargest(arr,K):
    h = []
    #add the first k elements into the heap(This is a min heap)
    for i in range(0,K):
        heapq.heappush(h,arr[i]) #KlogK
    for i in range(K,len(arr)): #n-k.log(n-k)
        if (arr[i]>h[0]):
            heapq.heappop()
            heapq.heappush(arr[i])
    return h[0]







