def can_make_same(num):
    count_0 = 0
    count_1 = 0
    for i in range(0,len(num)):
        if num[i]=='0':
            count_0 += 1
        else:
            count_1 += 1
    if count_0==1 or count_1==1:
        return True
    else:
        return False

test_cases = int(raw_input().strip())
for i in range(0,test_cases):
    num = raw_input().strip()
    if can_make_same(num):
        print "Yes"
    else:
        print "No"

