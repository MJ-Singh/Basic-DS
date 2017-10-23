class queue(object):
    
    def __init__(self):
        self.array = []
    def isempty(self):
        return self.array == []
    def insert(self,num):
        self.array.insert(0,num)
    def remove(self):
        print self.array.pop()
    
mj = queue()
mj.insert(9)
mj.insert(9)
mj.insert(8)
mj.insert(7)
mj.insert(6)
mj.insert(6)
mj.remove()
mj.remove()
mj.remove()
mj.remove()
mj.remove()
mj.remove()
print(mj.isempty())