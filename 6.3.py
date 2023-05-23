def main():
    array = list(map(int, input().split()))
    length = len(array)
    for i in range(length):
        if i == length // 2:
            print(*array)
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    print(*array)


if __name__ == "__main__":
    main()
