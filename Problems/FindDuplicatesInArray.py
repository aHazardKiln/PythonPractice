def findDuplicates(arr1,arr2):
    res = []
    for elem in arr1:
        if binarySearch(arr2,elem):
            res.append(elem)
    return res

# A1: [1, 9, 16, 4097]m
# A2: [1 ... 8192]n

#A2, 4096
#start=0, end=8191, mid=4096
#start=0, end=4095, mid=2047

#A2,4097
#start=0   , end=8191, mid=4096
#start=4097, end=8191, mid=6194
#start=?, end=?, mid=?
#start=?, end=?, mid=?

def binarySearch(arr, elem):
    start = 0
    end = len(arr)-1
    while(start<=end):#0<=3
        mid = (start + end)/2
        if arr[mid]==elem:
            return True
        elif elem<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return False