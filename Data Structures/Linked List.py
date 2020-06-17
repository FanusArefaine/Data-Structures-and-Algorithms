class node:

    def __init__(self, value):
        self.value = value 
        self.next = None


class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def push(self, value):

      
        if self.isEmpty():
            self.head = node(value)
            self.tail = self.head
            return

        new_node  = node(value)
        new_node.next = self.head
        self.head = new_node

       

    def append(self, value):

        if self.isEmpty():
            return self.push(value)

        new_node = node(value)
        self.tail.next = new_node
        self.tail = new_node


    # Insert a node with new_value after the node with target_value
    def insert_after(self, target_value, new_value):

        if self.isEmpty():
            print("The list is empty. Please push some values first!!")
            return

        new_node = node(new_value)
        
        # traversing over the list using curr and prev nodes
        curr = self.head
        prev = None

        while (curr.next != None and curr.value != target_value):
            curr = curr.next
        
        # If target_value is not available at the list
        if curr.next == None and curr.value != target_value:
            print("Target value is not available at the list!!")
            return

        prev = curr
        curr = curr.next

        # putting the new node after the node with target_value
        prev.next = new_node
        new_node.next = curr

    # A Function to delete a node with specific 'value'
    def delete(self, value):

        # Checking if the list is empty
        if self.isEmpty():
            print("The list is empty!!")
            return


        # Traversing the list to find the node with the specific value
        curr = self.head
        prev = None

        while (curr.next != None and curr.value != value):
            prev = curr
            curr = curr.next
        
        # Checking if the value is available at the list
        if (curr.next == None and curr.value != value):
            print("The value you are looking for is not in the list.")
            return
        
        # if the value is the first element at the list
        if self.head.value == value:
            self.head = self.head.next
            curr.next = None
            return

        prev.next = curr.next
        curr.next = None
        
    


    def print(self):

        curr = self.head

        while(curr != None):
            print(curr.value)
            curr = curr.next



    
        

my_list = Linked_List()

my_list.push(3)
my_list.push(4)
my_list.push(5)
my_list.insert_after(4, 8)
my_list.delete(5)

my_list.print()



           






