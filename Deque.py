class Deque(object):
    def __init__(self):
        self.mylist = []
    def addfront(self,item):
        self.mylist.append(item)
    def addrear(self,item):
        self.mylist.insert(0,item)
    def isEmpty(self):
        return self.mylist == []
    def removefront(self):
        return self.mylist.pop()
    def removerear(self):
        return self.mylist.pop(0)
    def size(self):
        return len(self.mylist)
    def ilist(self):
        return self.mylist
        
mj = Deque()
mj.addfront("mj")
mj.addrear(9)
mj.addfront(9)
mj.addrear(8)
mj.addfront(7)
mj.addrear(6)
mj.addfront(6)
mj.addrear(10)

print mj.removefront()
print mj.removerear()

print mj.ilist()
print mj.size()