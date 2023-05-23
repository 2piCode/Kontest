def generate_sequences(count_students: int, min_score: int, max_score: int, index: int, sequence: []) -> int:
    if len(sequence) == count_students:
        print(*sequence)
        return 1
    else:
        count = 0
        for i in range(min_score + count_students - index - 1, max_score + 1):
            count += generate_sequences(count_students, min_score, i - 1, index + 1, sequence + [i])
        return count


def main():
    count_students, min_score, max_score = map(int, input().split())
    count = generate_sequences(count_students, min_score, max_score, 0, [])
    print(count)


if __name__ == "__main__":
    main()
