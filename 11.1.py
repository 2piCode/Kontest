def get_neighbours(array: [], index: int, result: []) -> []:
    if index == -1:
        return result
    if index in result:
        return result
    result += [index]
    for i in array[index]:
        result = get_neighbours(array, i, result)
    return result


def main():
    n, v = map(int, input().split())
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))
    result = sorted(get_neighbours(array, v, []))
    print(*result)


if __name__ == "__main__":
    main()
