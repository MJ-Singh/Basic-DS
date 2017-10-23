def selectionsort(alist):
    for i in range(len(alist)-1 ,0 ,-1):
        pos_of_max = 0
        for location in range(1,i+1):
            if alist[location]>alist[pos_of_max]:
                pos_of_max = location
                
        temp = alist[i]
        alist[i] = alist[pos_of_max]
        alist[pos_of_max] = temp
        
alist = [1,2,31,3,4,12,44,4,9,3,2,35,]       
selectionsort(alist)
print alist