def f00(menu: [], money: int, dishes: [], index: int, calories: int):
    if money == 0 or index - 1 == len(menu):
        return dishes, calories
    else:
        without_next_dish = f00(menu, money, dishes, index + 1, calories)
        if money >= menu[index - 1][0]:
            with_next_dish = f00(menu, money - menu[index - 1][0], dishes + [index], index + 1, calories + menu[index - 1][1])
            return comparison_orders(with_next_dish, without_next_dish)
        else:
            return without_next_dish


def comparison_orders(first, second):
    if first[1] != second[1]:
        return first \
            if first[1] > second[1] \
            else second
    else:
        first_count = len(first[0])
        second_count = len(second[0])
        if first_count != second_count:
            return first \
                if first_count > second_count \
                else second
        else:
            first_first_index = 0
            second_first_index = 0
            for i in range(len(first[0])):
                first_first_index = first[0][i]
                second_first_index = second[0][i]
                if first_first_index != second_first_index:
                    break

            return first \
                if first_first_index < second_first_index \
                else second


def main():
    n, w = map(int, input().split())
    menu = []
    for i in range(n):
        price, caloric = map(int, input().split())
        menu.append((price, caloric))

    final_order = f00(menu, w, [], 1, 0)
    print(f"{len(final_order[0])} {final_order[1]}")
    print(*final_order[0])


if __name__ == "__main__":
    main()