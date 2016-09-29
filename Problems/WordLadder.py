import sys
from collections import deque
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        q = deque([(start,1,[start])])
        dictV.append(end)
        visited = set()
        min_len = sys.maxint
        while q:
            curr_word,length,ladder = q.popleft()
            visited.add(curr_word)
            if curr_word == end:
                if len(ladder)==min_len:
                    ladders.append(ladder)
                elif len(ladder)<min_len:
                    min_len = len(ladder)
                    ladders = [ladder,]
            #loop over the neighbors of current word
            for i in range(len(curr_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = curr_word[:i] + c + curr_word[i+1:]
                    if new_word in dictV and new_word not in visited:
                        q.append([new_word,length+1,ladder+[new_word]])
        return ladders








class Graph:
    def __init__(self,dictV):
        self.vertices = set()
        self.neighbors = {}
        #create the graph from dictV
        for word in dictV:
            self.addVertex(word)

    def addEdge(self,A,B):
        self.neighbors[A].add(B)
        self.neighbors[B].add(A)

    def addVertex(self,V):
        self.neighbors[V] = set()
        for vertex in self.vertices:
            if self.canTransform(V,vertex.val):
                self.addEdge(vertex.val,V)
        n = Node(V)
        self.vertices.add(n)
        return n

    def getPath(self,strA,strB):
        if strA == strB:
            return []
        q = []
        nA = self.addVertex(strA)
        nB = self.addVertex(strB)
        #refresh graph
        q.append(nA)
        q.append(0)
        nA.visited = True
        nA.idx = 0
        level = 0
        while (len(q)!=0):
            curr = q.pop(0)
            if curr == 0:
                level += 1
            else:
                for n in self.neighbors[curr.val]:
                    if n.visisted is False:
                        if n==nB:
                            pass
                        else:
                            n.idx = level
                            n.visisted = True
                            q.append(n)
                q.append(0)
        res = self.tracePath(nA,nB)
        return res







    '''scope for improvement'''
    def canTransform(self,s1,s2):
        letters_changed = 0
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                letters_changed += 1
        if letters_changed==1:
            return True
        else:
            return False

    def __str__(self):
        out = "Graph : \n"
        for vertex in self.vertices:
            out += vertex.val + "-> "
            for n in self.neighbors[vertex.val]:
                out += n + " "
            out += '\n'
        return out

class Node:
    def __init__(self,val):
        self.val = val
        self.idx = -1
        self.visited = False
    def __cmp__(self,other):
        return cmp(self.val,other.val)
    def __hash__(self):
        return hash(self.val)
    def __eq__(self,other):
        return self.val == other.val


sol = Solution()
print sol.findLadders("hit","cog",["hot","dot","dog","lot","log"])




