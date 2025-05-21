import time
import os

def print_bars(arr):
    sz = arr[0]
    os.system('clear')
    for val in arr:
        if val > sz:
            sz = val

    print("-" * (sz * 3))
    for height in range(sz, 0, -1):
        for value in arr:
            if value >= height:
                print(' ┃ ', end="")
            else:
                print("   ", end="")
        print()

    for val in arr:
        print(f"{val:^3}", end="")
    print()
    print("-" * (sz * 3))
    time.sleep(0.7)


def bubble_sort_visualize(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print_bars(arr)

data = [2, 10, 8, 1, 6, 4, 9, 3, 5]
bubble_sort_visualize(data)
