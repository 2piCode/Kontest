def get_max_height(gymnasts: list) -> int:
    gymnasts.sort(key=lambda x: ((x[1] + x[0]), x[1]))
    tower_gymnasts_by_weight = []
    total_weight = 0
    total_height = 0

    for weight_can_hold, weight in gymnasts:
        if weight_can_hold >= total_weight:
            total_height += 1
            total_weight += weight
            tower_gymnasts_by_weight.append(weight)
            tower_gymnasts_by_weight.sort()
        elif tower_gymnasts_by_weight[total_height - 1] > weight:
            temp_weight = tower_gymnasts_by_weight.pop()
            tower_gymnasts_by_weight.append(weight)
            tower_gymnasts_by_weight.sort()
            total_weight -= temp_weight - weight

    return total_height


def main():
    gymnasts_count = int(input())
    gymnasts = []
    for i in range(gymnasts_count):
        temp = input().split(";")
        weight_can_hold, weight = int(temp[1]), int(temp[2])
        gymnasts.append((weight_can_hold, weight))

    height = get_max_height(gymnasts)
    print(height)


if __name__ == "__main__":
    main()
