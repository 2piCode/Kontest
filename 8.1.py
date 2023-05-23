def partition(array: list, start_index: int, end_index: int):
    if end_index - start_index <= 1:
        return start_index
    i = start_index
    j = end_index - 1
    x = array[end_index - 1]
    print(x)
    while i <= j:
        while array[i] < x:
            i += 1
        while j > 0 and array[j] >= x:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        else:
            break

    array[i], array[end_index - 1] = array[end_index - 1], array[i]
    return i


def quick_sort(array: list, start_index: int, end_index: int):
    if end_index - start_index < 2:
        return
    middle_index = partition(array, start_index, end_index)
    quick_sort(array, start_index, middle_index)
    quick_sort(array, middle_index + 1, end_index)


def main():
    array = list(map(int, input().split()))
    quick_sort(array, 0, len(array))
    print(*array)


if __name__ == "__main__":
    main()
