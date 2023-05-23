def get_max_price(package_capacity: int, cakes: list) -> float:
    price = 0.0
    for cake_price, cake_capacity in cakes:
        if package_capacity < cake_capacity:
            price_by_unit_volume = cake_price / cake_capacity
            piece_price = package_capacity * price_by_unit_volume
            price += piece_price
            break
        else:
            price += cake_price
            package_capacity -= cake_capacity
    return price


def main():
    count_cakes, package_capacity = map(int, input().split())
    cakes = []
    for i in range(count_cakes):
        price, capacity = map(int, input().split())
        cakes.append((price, capacity))
    cakes.sort(key=lambda x: x[0] / x[1], reverse=True)
    cost = get_max_price(package_capacity, cakes)
    print(f"{cost:.2f}")


if __name__ == "__main__":
    main()
