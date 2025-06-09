
def all_even(arr: list) -> list:
    return [num for num in arr if num % 2 == 0]

if __name__ == "__main__":
    arr = []
    for i in range(1, 50 + 1):
        arr.append(i)

    print(all_even(arr))
