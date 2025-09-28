import Stack as st

def isMatch(a,b):

    if a == '{' and b == '}':
        return True
    elif a == '[' and b == ']':
        return True
    elif a == '(' and b == ')':
        return True
    else:
        return False

def isBalanced(braces):

    stack = st.Stack()
    opening = "({["
    close = ")}]"


    for bracket in braces:
        if bracket in opening:
            stack.push(bracket)
         
        elif bracket in close:
            if isMatch(stack.peek(),bracket):
                print(isMatch(stack.peek(),bracket))
                stack.pop()
               
    
    return stack.isEmpty()



print(isBalanced(")"))        # False