def seats(A):
    positions = []
    for i,c in enumerate(A):
        if c=='x':
            positions.append(i)
    if not positions:
        return 0
    median = len(positions)/2
    #print positions[median]
    #get all left
    pivot = positions[median]
    jumps=0
    for i in range(median-1,-1,-1):
        currSeat = positions[i]
        if currSeat==pivot-1:
            pivot = currSeat
            continue
        targetSeat = findFirstEmptyPlace(positions,pivot,-1)
        jumps += targetSeat-currSeat
        pivot = targetSeat
        print jumps
        positions.remove(currSeat)
        positions.insert(i,targetSeat)
    pivot=positions[median]
    for i in range(median+1,len(positions)):
        currSeat = positions[i]
        if currSeat==pivot+1:
            pivot = currSeat
            continue
        targetSeat = findFirstEmptyPlace(positions,pivot,1)
        jumps += currSeat-targetSeat
        pivot = targetSeat
        print jumps
        positions.remove(currSeat)
        positions.insert(i,targetSeat)

def findFirstEmptyPlace(seats,pos,direction):
    while pos in seats:
        pos+=direction
    return pos




seats("......")