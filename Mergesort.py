def mergesort(alist):
    print "Splitting ",alist
    if len(alist) > 1:
        mid = len(alist)/2
        leftlist = alist[:mid]
        rightlist = alist[mid:]
        
        mergesort(leftlist)
        mergesort(rightlist)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                alist[k] = leftlist[i]
                i = i + 1
            else:
                alist[k] = rightlist[j]
                j = j + 1
            k = k + 1
            
        while i < len(leftlist):
            alist[k] = leftlist[i]
            i = i + 1
            k = k + 1
            
        while j < len(rightlist):
            alist[k] = rightlist[j]
            j = j + 1
            k = k + 1
            
        print "Merrging ",alist
        
        
alist = [4,5,8,4,64,45,4,84,987]
mergesort(alist)
print(alist)
