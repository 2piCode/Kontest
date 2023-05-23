n = input()
m = input()

n_array = n.split()
m_array = m.split()

n_count = len(n_array)
height_indexes = {}

for i in range(0, n_count):
    height = n_array[i]
    if height not in height_indexes:
        height_indexes[height] = []
    height_indexes[height].append(i)

max_values = []
m_count = len(m_array)
for i in range(0, m_count):
    height = m_array[i]
    if height not in height_indexes.keys():
        max_values.append(0)
        continue

    count_indexes = len(height_indexes[height])
    max_value = 0
    for j, index in enumerate(height_indexes[height]):
        max_value = max((j + 1) * (n_count - (index + count_indexes - j)), max_value)
    max_values.append(max_value)


for i in range(len(max_values)):
    print(max_values[i], end=' ')