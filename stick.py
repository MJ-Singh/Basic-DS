a = int(raw_input())
for i in range(a):
    n = int(raw_input())
    s = raw_input()
    s = s.split()
    s = [int(x) for x in s]
    if len(s)<n or len(s)>n:
        print False
        break
    s.sort()
    s.reverse()
    nl = []
    j = 0
    while(j<len(s)-1):
        if s[j] == s[j+1]:
            k = s[j]
            nl.append(k)
            j = j + 2
        else:
            j = j + 1

    if len(nl) < 2:
        print False
        break
    print nl[0]*nl[1]    