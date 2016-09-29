import sys
def life_universe_everything():
    while True:
        inp = raw_input().strip()
        if inp != "42":
            print inp
        else:
            break

def nuclear_reactor():
    num_particles,M,R = map(int,raw_input().strip().split())
    l = [0]*R
    M = M+1
    for i in range(0,R):
        l[i] = (num_particles/(pow(M,i)))%M
    print " ".join(map(str,l))

def equalize():
    #Get the inputs
    M,N,Q = map(int,raw_input().strip().split())
    #build matrix
    mat = []
    for i in range(0,M):
        row = map(int,raw_input().strip().split())
        mat.append(row)
    #Take the queries and run the logic
    for i in range(0,Q):
        k,l = map(int,raw_input()) #rectangle for equalizing
        #real logic
        left_col = 0
        top_row = 0
        right_col = l-1
        bot_row = k-1
        max_median = -sys.max_int
        arr = fillElementsFromArr(mat,left_col,right_col,top_row,bot_row)
        while (bot_row<=M-1):
            median = arr[len(arr)/2]
            max_median = max(median,max_median)
            if right_col<N-1:

                #remove left from arr
                for i in range(0,k):
                    arr.remove(mat[top_row+i][left_col])
                left_col += 1
                right_col += 1
                #add right to arr
                for i in range(0,k):
                    arr.add(mat[top_row+i][right_col])
                arr.sort()
            else:
                #remove the elements from the top row
                for i in range(0,l):
                    arr.remove(mat[top_row][left_col+i])
                top_row += 1
                bot_row +=1
                #add bottom row elements to it
                for i in range(0,l):
                    arr.remove(mat[l])
                left_col = 0
                right_col = l-1


'''Returns sorted array from matrix indices '''
def fillElementsFromArr(mat,left_col,right_col,top_row,bot_row):
    l = []
    for i in range(top_row,bot_row+1):
        for j in range(left_col,right_col+1):
            l.add(mat[i][j])
    l.sort()
    return l


if __name__ == "__main__":
    nuclear_reactor()

