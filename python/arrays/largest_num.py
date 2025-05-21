
def find_large_number(arr: list[int]) -> int:
    if not arr:
        return 0
    large = arr[0]

    for i in range(len(arr)):
        if arr[i] >= large:
            large = arr[i]

    return large

if __name__ == "__main__":
    arr = [5, 7, 2, 10, 28, 1]
    print(find_large_number(arr))
    arr1 = []
    print(find_large_number(arr1))
