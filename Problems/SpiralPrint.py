def spiralOrder(A):
    result = []
    ## Actual code to populate result
    left_col = 0
    right_col = len(A[0])-1
    top_row = 0
    bottom_row = len(A)-1
    while(left_col<=right_col and top_row <= bottom_row):
        #Go left to right
        for i in range(left_col,right_col+1):
            result.append(A[top_row][i])
        top_row += 1
        #Go top to down
        for i in range(top_row,bottom_row+1):
            result.append(A[i][right_col])
        right_col-=1
        #right to left
        if (top_row<=bottom_row):
            for i in range(right_col,left_col-1,-1):
                result.append(A[bottom_row][i])
            bottom_row-=1
        #down to up
        if (left_col<=right_col):
            for i in range(bottom_row,top_row-1,-1):
                result.append(A[i][left_col])
            left_col+=1
    return result
print spiralOrder([
                    [1],
                    [3],
                    [5]
                ])