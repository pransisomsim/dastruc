import time
import os

class Node:
    def __init__(self, value):
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

def max_list(head):
    count = 0
    cur = head

    while cur:
        if cur.value > count:
            count = cur.value
        cur = cur.next

    return count

def traverse(head):
    cur = head

    while cur:
        print(f"{cur.value:^3}", end='')
        cur = cur.next

def print_bars(head):
    max_value = max_list(head)

    os.system('clear')
    for height in range(max_value, 0, -1):
        cur = head
        while cur:
            if cur.value >= height:
                print(' ┃ ', end='')
            else:
                print('   ', end='')
            cur = cur.next
        print()

    cur = head
    while cur:
        print('━━━', end='')
        cur = cur.next
    print()

    traverse(head)
def sort_linked_list_animated(head):
    if head is None or head.next is None:
        return head

    changed = True
    while changed:
        prev = None
        current = head
        changed = False

        while current and current.next:
            next_node = current.next

            if current.value > next_node.value:
                changed = True
                if prev is None:
                    # Swapping at head
                    current.next = next_node.next
                    next_node.next = current
                    head = next_node
                    prev = next_node
                else:
                    prev.next = next_node
                    current.next = next_node.next
                    next_node.next = current
                    prev = next_node
            else:
                prev = current
                current = current.next

        # Visualize after each outer loop pass
        print_bars(head)
        time.sleep(0.5)  # Pause for half a second to show progress

    return head

if __name__ == "__main__":
    head = Node(10)
    
    insert(head, 3)
    insert(head, 7)
    insert(head, 27)
    insert(head, 8)
    insert(head, 20)
    insert(head, 18)
    insert(head, 5)

    # traverse(head)
    print_bars(head)
