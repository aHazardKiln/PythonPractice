'''Input

The first line of input contains a single integer T denoting the number of test cases. This will be followed by T test cases.

The first line of each test case contains an integer N denoting the number of players.

The second line of each test case contains an integer c[i] denoting the number of cookies in the i-th storage, followed by c[i] space-separated integers type[i][j] which denote the type if j-th cookie in the storage i-th.

Output

For each test case, output a single line containing the answer as specified in the statement.

'''
def findWinner(fc):
    winner = -1
    max_points = -1
    res = []
    for i in range(0,len(fc)):
        extra = 0
        cookies = [c for c in fc[i]]
        while (len(set(cookies))>=4):
            cookies_set_len = len(set(cookies))
            if cookies_set_len<4:
                break
            if cookies_set_len==4:
                extra += 1
            elif cookies_set_len == 5:
                extra += 2
            elif cookies_set_len == 6:
                extra += 4
            for cookie in set(cookies):
                cookies.remove(cookie)
        points = len(fc[i])+extra
        res.append(points)
    for i in range(0,len(res)):
        if res[i]>max_points:
            max_points = res[i]
            winner = i
            tie = False
        elif res[i]==max_points:
            tie = True
    if tie is True:
        return -1
    else:
        return winner
T = int(raw_input().strip())

for i in range(0,T):
    num_of_players = int(raw_input().strip())
    l = []
    for i in range(0,num_of_players):
        cookies = map(int,raw_input().strip().split())
        l.append(cookies[1:])
    winner = findWinner(l)
    if winner == -1:
        print "tie"
    elif winner == 0:
        print "chef"
    else:
        print str(winner+1)