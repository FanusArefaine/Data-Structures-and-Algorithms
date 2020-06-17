# Stack implementation using list

class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    # Get the size of the stack
    def size(self):
        return self.size

    def isEmpty(self):
        if self.size==0:
            return True
        return False

    # get the number of elements of the stack
    def push(self, value):
        self.stack.append(value)
        self.size += 1

    # remove an element from the stack
    def pop(self):
        
        # Checking if the list is empty
        if self.isEmpty():
            print("The stack is empty!!")
            return

        self.stack.pop()
        self.size -= 1
    
    
    # A function that returns the top value of the stack
    def peek(self):
        #checking if the list is empty
        if self.isEmpty():
            print("The list is empty!!")
            return
        return self.stack[-1]

    def printStack(self):
        #checking if the list is empty
        if self.isEmpty():
            print("The list is empty!!")
            return
        
        for i in range(1, len(self.stack)+1):
            print(self.stack[-i])

        
if __name__=='__main__':

    my_stack = Stack()

    my_stack.push(4)
    my_stack.push(3)
    my_stack.push(2)
    my_stack.push(1)
    print("The stack has",my_stack.size,"items.")
    my_stack.printStack()



    

    




    
    



        
