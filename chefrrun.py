
m = int(raw_input())
my_list = []
for t in range(m):
    a = int(raw_input())
    b = raw_input()
    b = b.split()
    b = [int(x) for x in b]
    count = 0
    for i in range(a):
        j = b[i]
        k = (i+j+1)%a
        for s in range(a):
            if k==i:
                count = count + 1
                break
            else:
                k = (k + b[k] + 1) % a
    print count