from math import floor
heap_size = 0
def heap_sort(A):
    N=len(A)
    global heap_size
    heap_size = N
    build_heap(A)
    for i in range(N-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heap_size -=1
        max_heapify(A,0)
    return A


'''Creates a max heap'''
def build_heap(A):
    global heap_size
    for i in range(floor(heap_size/2),-1,-1):
        max_heapify(A,i)

'''Heapfies a max heap'''
def max_heapify(A,i):
    global heap_size
    parent = A[i]
    left = lambda x : (2*i)+1
    right = lambda y : (2*i)+2
    l = left(i)
    r = right(i)
    while(parent<left or parent<right):
        largest = left if left > parent else parent
        largest =

# Heapsort(A) {
#     BuildHeap(A)
#     for i <- length(A) downto 2 {
#       exchange A[1] <-> A[i]
#       heapsize <- heapsize -1
#       Heapify(A, 1)
#   }
#
#
#
# BuildHeap(A) {
#     heapsize <- length(A)
#     for i <- floor( length/2 ) downto 1
#       Heapify(A, i)
#   }
#
#
#
#
# Heapify(A, i) {
#       le <- left(i)
#       ri <- right(i)
#       if (le<=heapsize) and (A[le]>A[i])
#           largest <- le
#       else
#           largest <- i
#       if (ri<=heapsize) and (A[ri]>A[largest])
#           largest <- ri
#       if (largest != i) {
#           exchange A[i] <-> A[largest]
#           Heapify(A, largest)
#       }
#   }


