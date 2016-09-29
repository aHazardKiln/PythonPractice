def maxProduct(inp):
    #assumes inp has at least 3 numbers
    highest = max(inp[0],inp[1])
    lowest = min(inp[0],inp[1])
    highest2 = inp[0]*inp[1]
    lowest2 = inp[0]*inp[1]
    highest3 = None
    for curr in inp[2:]:
        for x in [highest2,lowest2]:
            prod = curr*x
            if highest3==None:
                highest3=curr*x
            elif prod > highest3:
                highest3 = prod
        for x in [highest,lowest]:
            prod = curr*x
            #update highest or lowest product
            if prod > highest2:
                highest2 = prod
            if prod < lowest2:
                lowest2 = prod
        #update highest and lowest for the next iteration
        if curr > highest:
            highest = curr
        if curr < lowest:
            lowest = curr
    return highest3
print maxProduct([0,-1,2,3,5])

'''
highest:2
lowest:1
highest2:2
lowest2:2
highest3:
'''

