def main():
    count_types = int(input())
    bacteria_temperature = []
    for i in range(count_types):
        bacteria_temperature.append(tuple(map(int, input().split())))

    temperatures_by_planet = list(map(int, input().split()))
    result = []
    for i in temperatures_by_planet:
        count = 0
        for j in bacteria_temperature:
            if j[0] <= i <= j[1]:
                count += 1
        result.append(count)

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
