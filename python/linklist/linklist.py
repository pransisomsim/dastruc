
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
def insert(head, value: int):
    new = Node(value)
    if head.value is None:
        head.value = value
        return

    cur = head
    while(cur.next):
        cur = cur.next
    cur.next = new

def display(head):
    cur = head
    print("Linklist: ", end="")
    while(cur):
        print(f"{cur.value} -> ", end="")
        cur = cur.next

if __name__ == "__main__":
    head = Node(10)
    insert(head, 20)
    insert(head, 30)
    insert(head, 40)
    insert(head, 50)

    display(head)
