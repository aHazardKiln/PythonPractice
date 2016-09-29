Question: Given an array A of size N, rearrange the array such that
A[i] = A[A[i]]. Do this in O(1) space.
0 to N-1

9 elements,

0 5 6 8 1 2 5 3 4
0 1 2 3 4 5 6 7 8

0 2 5 4 5 6 2 8 1
A[0] = 0 * 9 + 0 = 0
A[1] = 2 * 9 + 5 = 23
A[2] = 5 * 9 + 6 = 51
A[3] = 4 * 9 + 8 = 44
A[4] = 5(=(A[A[4]]%9)) * 9 + 1 = 46



for i in range(0,len(A)):
    New = A[i]
    A[i] = (A[New]%9) * 9 + A[i]

for i in range(0,len(A)):
    A[i] = A[i]/9


original
New =

New * 9 + Original

New = Val / 9
Original = Val % 9



Example 2:
3 1 1 0
0 1 2 3

0 1 1 3