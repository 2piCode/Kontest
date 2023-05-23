def main():
    array = list(map(int, input().split()))
    num = int(input())
    length = len(array)
    for i in range(length):
        if i == num:
            print(*array)
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print(*array)


if __name__ == "__main__":
    main()
