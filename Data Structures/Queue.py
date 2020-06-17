class Queue:

    def __init__(self):
        self.queue = []
    
    # check if the queue is empty
    def isEmpty(self):
        return self.queue == []
    
    # add an element to the queue
    def enqueue(self, value):
        self.queue.insert(0,value)

    # remove an element from the queue
    def dequeue(self):
        self.queue.pop()

    # Returns the size of the queue
    def size(self):
        return len(self.queue)

    def printQueue(self):

        # Check if the queue is empty
        if self.isEmpty():
            print("The queue is empty!!!")
            return
        
        for i in range(0, len(self.queue)):
            print(self.queue[i])



if __name__ == '__main__':

    my_queue = Queue()
    
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    my_queue.dequeue()
    my_queue.printQueue()


