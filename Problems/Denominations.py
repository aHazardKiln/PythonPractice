def no_of_ways_helper(denominations,M):
    #sanity checks
    if (M==0):
        return 1
    if (M<0) or len(denominations)==0:
        return 0

    ways = 0
    deno = denominations[0]
    for i in range(0,(M/deno)+1):
        ways += no_of_ways_helper(denominations[1:],M-(deno*i))
    return ways
def no_of_ways(denominations,M):
    denominations = sorted(denominations)
    denominations.reverse()
    return no_of_ways_helper(denominations,M)
print no_of_ways([3,2,1],4)