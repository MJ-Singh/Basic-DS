class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
def in_to_post(instr):
    s = Stack()
    tokenlist = instr.split()
    postfixlist = []
    prev = {"*":3, "/":3, "+":2, "-":2, "(":1}
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            toptoken = s.pop()
            while toptoken != '(':
                postfixlist.append(toptoken)
                toptoken = s.pop()
        else:
            while (not s.isEmpty()) and prev[s.peek()] >= prev[token]:
                postfixlist.append(s.pop())
            s.push(token)
    while not s.isEmpty():
        postfixlist.append(s.pop())
    print " ".join(postfixlist)


in_to_post("( A * B ) + ( B / C * D )")   
  
    