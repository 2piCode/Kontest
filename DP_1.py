def max_sum_coins(city: [], n: int, m: int):
    sum_coins = [[0] * m for _ in range(n)]
    sum_coins[0][0] = city[0][0]

    for i in range(1, n):
        sum_coins[i][0] = sum_coins[i - 1][0] + city[i][0]

    for i in range(1, m):
        sum_coins[0][i] = sum_coins[0][i - 1] + city[0][i]

    for i in range(1, n):
        for j in range(1, m):
            sum_coins[i][j] = max(sum_coins[i - 1][j], sum_coins[i][j - 1]) + city[i][j]

    return sum_coins[n - 1][m - 1]


def main():
    n, m = map(int, input().split())
    city = []
    for i in range(n):
        line = list(map(int, input().split()))
        city.append(line)

    print(max_sum_coins(city, n, m))


main()
