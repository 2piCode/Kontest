from collections import Counter


def print_array(array: list):
    for i in range(0, len(array)):
        print(array[i], end="")


def get_sum_array(array: list, weights: dict, length_middle_part: int):
    sum = 0
    for i, j in enumerate(array):
        sum += (length_middle_part + i * 2 + 1) * weights[j]
    return sum


def main():
    s = input()
    symbols_amount = Counter(sorted(list(s)))
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    temp = input().split(" ")
    weights = {}
    for i in range(0, len(alphabet)):
        weights[alphabet[i]] = int(temp[i])

    result = []
    temp_array = []
    for symbol, amount in symbols_amount.items():
        if amount < 2 or weights[symbol] <= 0:
            for i in range(amount):
                temp_array.append(symbol)
        else:
            result.append(symbol)
            for i in range(amount - 2):
                temp_array.append(symbol)

    result.sort(key=lambda x: (weights[x], -ord(x)))
    length_middle_part = len(temp_array)
    sum = get_sum_array(result, weights, length_middle_part)
    print_array(result[::-1])
    print_array(temp_array)
    print_array(result)
    print(f" {sum}")


if __name__ == "__main__":
    main()
