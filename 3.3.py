def check_index(index: int, tiles: []) -> bool:
    for i in range(index):
        if tiles[index - (i + 1)] != tiles[index + i]:
            return True
    return False


a = input().split()
n, m = int(a[0]), int(a[1])
tiles = input().split()

indexes = []
for index in range(n // 2 + 1):
    if not check_index(index, tiles):
        indexes.append(n - index)


for i in range(len(indexes)):
    print(indexes[i], end=" ")