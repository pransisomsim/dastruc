class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next

    def getPrev(self):
        return self.__prev
    
    def setNext(self, next):
        self.__next = next

    def setPrev(self, prev):
        self.__prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__current = None

    def isEmpty(self):
        return self.__head is None and self.__tail is None

    def insert(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.__head = self.__tail = new_node
            self.__current = new_node
        else:
            new_node.setPrev(self.__tail)
            self.__tail.setNext(new_node)
            self.__tail = new_node

    def next(self):
        if self.__current and self.__current.getNext():
            self.__current = self.__current.getNext()
            return self.__current.getData()
        return None

    def prev(self):
        if self.__current and self.__current.getPrev():
            self.__current = self.__current.getPrev()
            return self.__current.getData()
        return None

    def current(self):
        if self.__current:
            return self.__current.getData()
        return None

    def display(self):
        if self.isEmpty():
            print("List is empty")
            return
        current = self.__head
        while current:
            print(f"[ {current.getData()} ]", end=" <-> ")
            current = current.getNext()
        print("None")
