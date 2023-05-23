def derivative(x: float, a: float, v0: int, vs: int) -> float:
    return (v0 * x) / ((x ** 2 + (1 - a) ** 2) ** 0.5) + (vs * (x - 1)) / (((1 - x) ** 2 + a ** 2) ** 0.5)


buf = input().split()
v0, vs = int(buf[0]), int(buf[1])
s = int(input())

a = s / 100
left_border, right_border = 0, 1
eps = 10 ** -6
position = None

while abs(derivative(right_border, a, v0, vs) - derivative(left_border, a, v0, vs)) > eps:
    middle = (left_border + right_border) / 2
    if derivative(middle, a, v0, vs) == 0 or abs(derivative(middle, a, v0, vs)) < eps:
        position = middle
        break
    elif derivative(left_border, a, v0, vs) * derivative(middle, a, v0, vs) < 0:
        right_border = middle
    else:
        left_border = middle

print(f"{abs(1 - position):.0{6}f}")