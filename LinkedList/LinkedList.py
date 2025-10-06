from Node import Node


class LinkedList():
    
    print("Entering List Class")
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while(lastNode.next):
                lastNode = lastNode.next
            
            lastNode.next = newNode

    def prepend(self,data):

        newNode = Node(data)
        lastHead = self.head
        self.head = newNode
        self.head.next = lastHead

    def insertAfterNode(self,prevNode, data):

        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def printList(self):
        
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self,key):
        
        currNode = self.head

        if currNode and currNode.data == key:
            self.head = currNode.next
            currNode = None
            return
        
        prev = None
        while currNode and currNode.data != key:
            prev = currNode
            currNode = currNode.next

        if currNode is None:
            return

        prev.next = currNode.next
        currNode = None

    def delPos(self,i):

        currNode = self.head
        print("Entered del")
        if i == 0:
            self.head = self.head.next
            currNode = None
            return
        
        prevNode = None
        for count in range(i):
            prevNode = currNode
            currNode = currNode.next

        prevNode.next = currNode.next
        currNode = None

    def length(self):

        count = 0
        curr = self.head
        if curr is None:
            return count
        
        while curr:
            count += 1
            curr = curr.next
        
        return count
    
    def lenRecursive(self, node):
        if node is None:
            return 0
        return 1 + self.lenRecursive(node.next)
    
    def reverse(self):

        curr = self.head
        while curr:
            oldNext = curr.next
            

        

newlist = LinkedList()
newlist.append(1)
newlist.append(2)
newlist.append(3)
newlist.append(4)
newlist.append(5)
print(newlist.length())
print("****************")
print(newlist.lenRecursive(newlist.head))



