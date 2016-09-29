def is_overlapping(x,y):
    if (x[1]<y[0]):
        return False
    return True
def my_function(arg):
    # write the body of your function here
    arg = sorted(arg,key=lambda x : (x[0],x[1]))
    x=0
    while x < len(arg)-1:
        curr = arg[x]
        nex = arg[x+1]
        if is_overlapping(curr,nex):
            t = (min(curr[0],nex[0]),max(curr[1],nex[1]))
            del arg[x]
            del arg[x]
            arg.insert(x,t)
        else:
            x+=1
    return 'running with %s' % arg

# run your function through some test cases here
# remember: debugging is half the battle!
args =   [(1, 10), (2, 6), (3, 5), (7, 9)]
print my_function(args)
