def kth_search(array: list, start_index: int, end_index: int, k: int) -> int:
    x = array[(start_index + end_index) // 2]
    i, j = start_index, end_index

    while i <= j:
        while array[i] < x:
            i += 1
        while array[j] > x:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if start_index <= k <= j:
        return kth_search(array, start_index, j, k)
    if i <= k <= end_index:
        return kth_search(array, i, end_index, k)

    return array[k]


def main():
    array = list(map(int, input().split()))
    k = int(input())
    print(kth_search(array, 0, len(array) - 1, k))


if __name__ == "__main__":
    main()