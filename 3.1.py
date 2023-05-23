array1 = input().split()
array2 = input().split()

values = {}
for i in range(0, len(array2)):
    value = array2[i]
    if value not in values:
        values[value] = []
    values[value].append(i)

for i in range(0, len(array1)):
    value = array1[i]
    if value not in values:
        print(0, end=' ')
        continue
    print(len(values[value]), end=' ')