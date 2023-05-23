def plus(num1: int, num2: int) -> int:
    return num1 + num2


def minus(num1: int, num2: int) -> int:
    return num1 - num2


def multiplication(num1: int, num2: int) -> int:
    return num1 * num2


def division(num1: int, num2: int) -> int:
    return num1 // num2


def remainder_division(num1: int, num2: int) -> int:
    return num1 % num2


def main():
    operators = {'+': plus, '-': minus, '*': multiplication, '/': division, '%': remainder_division}
    function = input().split(" ")
    stack = []
    for elem in function:
        if elem == ' ':
            continue
        elif elem.isdigit():
            stack.append(elem)
        else:
            num1, num2 = stack.pop(), stack.pop()
            stack.append(operators[elem](int(num2), int(num1)))
    print(stack.pop())


if __name__ == "__main__":
    main()
