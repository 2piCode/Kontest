def is_correct_str(s_hash: int, s_count: int, b_hash: int, b_count: int) -> bool:
    if s_count % b_count != 0:
        return False
    if s_hash != b_hash * (s_count // b_count):
        return False

    return True


def get_hash_char(a: chr) -> int:
    return ord(a)


def get_hash_string(a: str) -> int:
    hash = 0
    for i in range(0, len(a)):
        hash += ord(a[i])

    return hash


s = input()

s_hash = get_hash_string(s)
s_count = len(s)
max_str = None
b_hash = 0
for i in range(0, s_count // 2 + 1):
    b_hash += get_hash_char(s[i])
    if is_correct_str(s_hash, s_count, b_hash, i + 1):
        max_str = s[0:i+1]
        break

if max_str is not None:
    print(f"{len(s) // len(max_str)} {max_str}")
else:
    print(f"1 {s}")