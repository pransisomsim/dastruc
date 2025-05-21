
class Node:
    def __init__(self, value) -> None:
        self.value = value if value else None
        self.next = None

class LinkedList:
    def __init__(self, head=None) -> None:
        self.__head = head if head else None

    def insert(self, value: int) -> None:
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        cur = self.__head

        while(cur.next):
            cur = cur.next
        cur.next = new

    def display(self) -> None:
        cur = self.__head

        while(cur):
            print(f"{cur.value} -> ", end="")
            cur = cur.next

    def get_head(self):
        return self.__head

def merge_list(list1, list2):
    head = list1.get_head()
    if head is None:
        return LinkedList(list2.get_head())

    cur = head
    while(cur.next):
        cur = cur.next
    cur.next = list2.get_head()

    return LinkedList(head)

if __name__ == "__main__":
    link1 = LinkedList()
    link1.insert(5)
    link1.insert(10)
    link1.insert(15)
    link1.insert(20)
    link1.insert(25)

    link1.display()

    print("\n")

    link2 = LinkedList()
    link2.insert(2)
    link2.insert(4)
    link2.insert(6)
    link2.insert(8)
    link2.insert(10)

    link2.display()

    link3 = merge_list(link1, link2)
    print("\nMerge list: ")
    link3.display()
