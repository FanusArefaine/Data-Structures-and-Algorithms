class Node:

    """ This is a Node class with only a constructor.
    """

    def __init__(self, data):
        self.data = data 
        self.next = None 
    

class LinkedList():

    """ This is a Linked List class with several methods.
    """

    def __init__(self):
        self.head = None 
        self.tail = None

    # check if the linked list is empty 
    def isEmpty(self):
        return True if self.head == None else False 


        # Printing the elements of a linked list 
    
    def printList(self):

        if not self.isEmpty():
            
            curr = self.head 

            while curr != None:
                print(curr.data, end=" ")
                curr = curr.next
            return 

        print("The list is empty") 



    # Inserting elements in the front of a linked list 
    def insertFront(self, data):

        newNode = Node(data)

        if self.isEmpty():
            self.head = newNode 
            self.tail = self.head

        else:
            newNode.next = self.head 
            self.head = newNode 
    


    def insertLast(self, data):

        newNode = Node(data)

        if self.isEmpty():
            self.head = self.tail = newNode
        
        else:
            self.tail.next = newNode
            self.tail = newNode

    
    # Insert a node after a node with a 'target' value     
    def insertAfter(self, target, data):

        if not self.isEmpty():

            curr = self.head 
            trail = None 

            while curr != None:

                if curr.data == target:
                    break 
                curr = curr.next 
            
            if not curr == None:

                newNode = Node(data)
                newNode.next = curr.next 
                curr.next = newNode
                
            
        print("Empty List")


    
    # Delete a node with a value 'data'
    def deleteNode(self, data):

        if not self.isEmpty():

            if self.head.data == data:
                self.head = self.head.next
            
            else:

                curr = self.head 

                while curr.next != None:

                    if curr.next.data == data:
                        curr.next = curr.next.next
                        return 
                    curr = curr.next 
        
        print("Empty List")






        

    

        


    
        
    




if __name__ == '__main__':

    l = LinkedList()
    print(l.isEmpty())
    l.printList()
    l.insertAfter(4, 87)

    l.insertFront(4)
    l.insertFront(3)
    l.insertFront(8)
    l.insertFront(9)
    l.insertLast(88)
    l.insertLast(2)
    l.insertAfter(4, 87)
    l.deleteNode(9)
    print()
    print(l.isEmpty())
    l.printList()
        