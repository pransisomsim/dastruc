class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    def setNext(self, next):
        self.__next = next

class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None

    def isEmpty(self):
        return self.__front is None and self.__rear is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.__rear is None:
            self.__front = self.__rear = new_node
            return
        self.__rear.setNext(new_node)
        self.__rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print('Queue underflow.')
            return
        
        temp = self.__front
        self.__front = temp.getNext()
        if self.__front is None:
            self.__rear = None
            
        return temp.getData()

    def peek(self):
        if self.isEmpty():
            print('Queue underflow.')
            return
        
        return self.__front.getData()

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current = self.__front
        while current:
            print(current.getData(), end=" -> ")
            current = current.getNext()
        print("None")
