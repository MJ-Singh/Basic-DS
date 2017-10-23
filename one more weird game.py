a = int(raw_input())
for j in range(a):
    a = int(raw_input())
    b = int(raw_input())
    k = a*b
    l = []
    count = 0
    i = 0
    while(i<k):
        l.append(1)
        for m in range(a):
            if i<b*(m+1) and i>b*m and i-1>=0 and l[i-1] == 1:
                count += 1
        if i-b>=0 and l[i-b] == 1:
            count += 1  
        i += 1
    print count