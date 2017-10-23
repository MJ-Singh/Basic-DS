a = int(raw_input())
for i in range(a):
    n = int(raw_input())
    s1 = raw_input()
    s2 = raw_input()
    l1 = list(s1)
    l2 = list(s2)
    new_list = []
    if len(l1) != len(l2) or len(l1) != n:
        print "-1"
        break
    for j in range(n):
        if l1[j] == l2[j] and l1[j] =='W':
            new_list.append('B')
        elif l1[j] == l2[j] and l1[j] =='B':
            new_list.append('W')
        else:
            new_list.append('B')
    print ''.join(new_list)