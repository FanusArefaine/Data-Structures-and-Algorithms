class Queue:

    def __init__(self):
        self.queue = []
    
    # check if the queue is empty
    def isEmpty(self):
        return self.queue == []
        
    
    # add an element to the queue
    def enqueue(self, value):
        self.queue.append(value)
       

    # remove an element from the queue
    def dequeue(self):
        del self.queue[0]
        

    # Returns the size of the queue
    def size(self):
        return len(self.queue)
        

    def printQueue(self):
        print(self.queue)

     



if __name__ == '__main__':

    my_queue = Queue()
    
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    my_queue.dequeue()
    my_queue.enqueue(9)
    my_queue.printQueue()


