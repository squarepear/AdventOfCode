def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    data = lines[0].strip().split(',')

    fishes = [0] * 9

    for inp in data:
        fishes[int(inp)] += 1



    for i in range(256):
        temp = [0] * 9

        for j in range(8):
            temp[j] = fishes[j + 1]

        temp[6] += fishes[0]
        temp[8] += fishes[0]

        fishes = temp.copy()
        
        print(f"iter: {i + 1}")

    for count in fishes:
        result += count

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
