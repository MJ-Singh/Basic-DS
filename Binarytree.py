class Binarytree:
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None
    
    def insertleft(self, newnode):
        if self.leftchild == None:
            self.leftchild = Binarytree(newnode)
        else:
            t = Binarytree(newnode)
            t.leftchild = self.leftchild
            self.leftchild = t
    
    def insertright(self, newnode):
        if self.rightchild == None:
            self.rightchild = Binarytree(newnode)
        else:
            t = Binarytree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t
    
    def getrightchild(self):
        return self.rightchild
        
    def getleftchild(self):
        return self.leftchild  
        
    def setrootval(self, obj):
        self.key = obj
        
    def getrootval(self):
        return self.key
        
        
r = Binarytree('a')
print(r.getrootval())
print(r.getleftchild())
r.insertleft('b')
print(r.getleftchild())
print(r.getleftchild().getrootval())
r.insertright('c')
print(r.getrightchild())
print(r.getrightchild().getrootval())
r.getrightchild().setrootval('hello')
print(r.getrightchild().getrootval())