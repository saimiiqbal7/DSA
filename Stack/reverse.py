import Stack

def reverse(str):

    stack = Stack.Stack()
    for letter in str:
        stack.push(letter)
    
    new = ""

    while not stack.isEmpty():
        new += stack.pop()
        
     
    
    return new

print(reverse("hello"))
