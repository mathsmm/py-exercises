def run_length_decode(list: list):
    result = []
    i = 0
    while i < len(list) - 1:
        char = list[i]
        count = list[i+1]
        for j in range(count):
            result.append(char)
        i += 2

    return result


def main():
    list = ["A", 12, "B", 4, "A", 6, "B", 1]
    print(run_length_decode(list))

if __name__ == "__main__":
    main()