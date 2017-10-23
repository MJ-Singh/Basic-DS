class stack(object):
    def __init__(self):
        self.array = []
    def isempty(self):
        return self.array == []
    def push(self,num):
        self.array.append(num)
    def pop(self):
        print self.array.pop()
    
mj = stack()
mj.push(9)
mj.push(9)
mj.push(8)
mj.push(7)
mj.push(6)
mj.push(6)
mj.pop()
mj.pop()
mj.pop()
mj.pop()
mj.pop()
mj.pop()
print(mj.isempty())