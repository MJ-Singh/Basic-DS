def insertionsort(alist):
    for i in range(1,len(alist)):
    
        currentvalue = alist[i]
        position = i
        
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
            
        alist[position] = currentvalue
        
alist = [2,32,5,2,9,2,53,35,8,34,23,6,7,87,6,7,65]
insertionsort(alist)
print alist