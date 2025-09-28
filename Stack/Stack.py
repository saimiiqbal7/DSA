
class Stack():

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return ""

    def getStack(self):
        return self.items
    
    def isEmpty(self):
        return len(self.items) == 0
    


