def main():
    array = list(map(int, input().split()))
    length = len(array)
    for i in range(1, length):
        if i == length // 2 + length % 2:
            print(*array)
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    print(*array)


if __name__ == "__main__":
    main()
