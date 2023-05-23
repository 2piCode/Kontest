def merge(array: list, left: int, middle: int, right: int):
    global count

    left_pointer, right_pointer = left, middle
    result_pointer = 0
    temp_array = [0] * (right - left)

    while left_pointer < middle or right_pointer < right:
        if left_pointer == middle:
            temp_array[result_pointer] = array[right_pointer]
            right_pointer += 1
            result_pointer += 1
            continue
        if right_pointer == right:
            temp_array[result_pointer] = array[left_pointer]
            left_pointer += 1
            result_pointer += 1
            continue
        if array[left_pointer] < array[right_pointer]:
            temp_array[result_pointer] = array[left_pointer]
            result_pointer += 1
            left_pointer += 1
        else:
            temp_array[result_pointer] = array[right_pointer]
            count += middle - left_pointer
            result_pointer += 1
            right_pointer += 1

    for i in range(left, right):
        array[i] = temp_array[i - left]


def merge_sort(array: list, left: int, right: int = None):
    if right is None:
        right = len(array)
    if right - left <= 1:
        return 0
    middle = (left + right) // 2
    merge_sort(array, left, middle)
    merge_sort(array, middle, right)
    merge(array, left, middle, right)


def main():
    length = int(input())
    array = []
    for i in range(length):
        array.append(int(input()))

    merge_sort(array, 0)
    print(count)


if __name__ == "__main__":
    count = 0
    main()
