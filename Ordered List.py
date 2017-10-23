class Node(object):
    def __init__(self,item):
        self.data = item
        self.next = None
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self, newdata):
        self.data = newdata
    def setnext(self, newnext):
        self.next = newnext
        
class OrderedList(object):
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        current = self.head
        stop = False
        previous = None
        while current != None and not stop :
            if current.getdata() >= item:
                stop = True
            else: 
                previous = current
                current = current.getnext()
        temp = Node(item)
        if previous == None:
            temp.setnext(self.head)
            self.head = temp
        else:
            temp.setnext(current)
            previous.setnext(temp)
    def size(self):
        current = self.head
        count = 0
        while current != None :
            count = count + 1
            current = current.getnext()
        return count
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getdata() > item :
                stop = True
            else:
                if current.getdata() == item:
                    found = True
                else:
                    current = current.getnext()
        return found
    def remove(self,item):
        current = self.head
        found = False
        previous = None
        while not found:
            if current.getdata() == item :
                found = True
            else:
                previous = current
                current =  current.getnext()
        if previous == None :
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())        
    def seelist(self):
        current = self.head
        a = []
        while current != None:
            a.append(current.getdata())
            current = current.getnext()
        b = [str(x) for x in a]
        print " --> ".join(b)    
        
mj = OrderedList()

print mj.isEmpty()

mj.add(12)
mj.add(7)
mj.add(7)
mj.add(45)
mj.add(254)
mj.add(5)
mj.add(23)
mj.add(409)
mj.add(876)

mj.seelist()

print mj.isEmpty()

print mj.size()

mj.remove(254)

print mj.size()

mj.seelist()