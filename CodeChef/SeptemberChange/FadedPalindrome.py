'''
Problem code: LEXOPAL
Input
    First line of input contains a single integer T denoting the number of test cases. T test cases follow.
    First and the only line of each case contains string s denoting the old string that chef has found in his garage.
Output
    For each test case, print lexicographically smallest palindrome after filling each faded character - if it possible to construct one. Print -1 otherwise.
'''
def lex_smallest_string(inpt):
    inp = list(inpt)
    n = len(inp)
    for i in range(0,n/2):
        left = i
        right = n-1-i
        if inp[left]=="." and inp[right]==".":
            inp[left] = 'a'
            inp[right] = 'a'
        elif inp[left]=="." or inp[right]==".":
            if inp[left]==".":
                inp[left]=inp[right]
            else:
                inp[right]=inp[left]
        elif inp[left]!=inp[right]:
            return str(-1)
    if (n%2 == 1):
        if inp[n/2]==".":
            inp[n/2]="a"
    return "".join(inp)

T = int(raw_input().strip())
for i in range(0,T):
    print lex_smallest_string(raw_input().strip())
