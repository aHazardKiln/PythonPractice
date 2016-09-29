def my_reverse(arr, start,end):
    word_len = end-start+1
    for i in range(0,(word_len/2)):
        arr[start+i],arr[end-i] = arr[end-i],arr[start+i]
    return arr

def sentReverse(arr):
    #reverse the entire string
    arr = my_reverse(arr,0,len(arr)-1)
    start = 0
    end = 0
    while (end<len(arr)):
        while(end<len(arr) and arr[end]!=" "):
            end += 1
        arr = my_reverse(arr,start,end-1)
        start = end+1
        end += 1
    return arr
arr = list("practice makes perfect")
print sentReverse(arr)




    # // for every word in the list of characters:
    # //       add it to the list of words


    # // reverse the list
    # // create an array of characters

    # // O(mn)
    # // O(mn)
    # // reverseWord(L, start, end)


    # // cat goes here
    # // here goes cat

    # // ereh seog tac
    # // i = start
    # // j = start
    # // while(i and j are less than len(str)):
    # //       find the end of current word
    # //       reverse the word
    # //       change i