"""
Exercise 1:
    Given a linked list with year 2000 - 2050,
    create a function that would return a new set of linkedlist
    containing leap years from the given years.
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def is_leap(value):
    return value % 4 == 0 and value / 100 != 0

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
    while(cur):
        print(f"{cur.value} -> ", end="")
        cur = cur.next

def get_leap(head):
    if not head:
        return

    leap = Node(None)
    cur = head
    while(cur):
        if is_leap(cur.value):
            insert(leap, cur.value)
        cur = cur.next

    return leap

if __name__ == "__main__":
    head = Node(None)
    
    for i in range(2000, 2050):
        insert(head, i)
    print("Given years: ")
    display(head)

    print("\n")

    leap = get_leap(head)
    print("Leap years: ")
    display(leap)
