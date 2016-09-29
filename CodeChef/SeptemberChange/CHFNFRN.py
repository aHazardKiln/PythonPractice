'''
Chef invited N of his friends in his birthday party. All the friends are numbered from 1 to N. Some of the friends might know each other. You are given this information by M pairs each of form (ai, bi), denoting that the persons ai and bi know each other.
Chef wants all of his guests to seat at the two tables set up for dinner. He wants that all the people sitting at a table must know each other, otherwise they will feel awkward with mutual eating habits. Chef is okay if a table is not occupied by any person. Chef is worried whether all the guests can seat at the dinner tables in the desired way.
Please help Chef fast to identify whether his worry is real or not!! The delicacies at the table are getting cold.
Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M, denoting the number of Chef's friends and the number of pairs representing information whether two person know each other or not.
The next M lines contain two space-separated integers ai and bi, denoting that persons ai and bi know each other.
Output
For each test case, output a single line containing word "YES" (without quotes) if Chef can divide all of his friends into two groups that in each group all the people know each other and "NO" (without quotes) otherwise.
'''
class Table:
    def __init__(self,idx):
        self.index = idx
        self.peeps = set()

    def seat(self,guest):
        self.peeps.add(guest)

    def __str__(self):
        return "T"+self.index+":"+str(self.peeps)

'''Try seating a person on a table and seat him if you can'''
def trySeat(table,guest,friendship):
    for seated in table.peeps:
        if friendship[seated][guest] is False:
            return False
    return True


def canSeatOnTwoTables(people,friendship):
    #edge cases
    if len(people)<=2:
        return True

    # initialize the two tables
    T1 = Table(1)
    T2 = Table(2)

    # seat the first guy
    first_guest = people.pop(0)
    T1.seat(first_guest)

    # Waiting for T1
    q1 = []
    #who will definitely sit on T2
    while (len(people)!=0):
        guest = people.pop(0)
        if trySeat(T1,guest,friendship) is False:
            if trySeat(T2,guest,friendship) is False:
                return False
            else:
                T2.seat(guest)
        else:
            q1.append(guest)

    # check for second table rejects the table 1 candidates
    rumba = []
    while True:
        orig_len = len(q1)
        i = 0
        while i < len(q1):
            guest = q1[i]
            if trySeat(T2,guest,friendship) is False:
                #should definitely be in T1
                if friendship[first_guest][guest] is False:
                    return False
                T1.seat(guest)
                first_guest = guest
                del q1[i]
            else:
                i += 1
        if len(q1)==orig_len:
            break

    # seat the guests in T1 and T2 if possible
    return canSeatOnTwoTables(q1,friendship)


'''Initialize 2-D adjacency matrix of friends'''
def initializeFriends(num_of_friends):
    people = []
    friendship = [[False for i in range(0,num_of_friends+1)] for i in range(0,num_of_friends+1)]
    for i in range(1,num_of_friends+1):
        friendship[i][i] = True
        people.append(i)
    return friendship,people

def buildFriends(friendship,a,b):
    friendship[a][b] = True
    friendship[b][a] = True
    return

if __name__ == "__main__":
    T = int(raw_input().strip())
    for t in range(0,T):
        N,M = map(int,raw_input().strip().split())
        friendship,people = initializeFriends(N)
        for i in range(M):
            a,b = map(int,raw_input().strip().split()) #a,b know each other
            buildFriends(friendship,a,b)
        #execute
        print "YES" if canSeatOnTwoTables(people,friendship) else "NO"
