def basin(field, lines, x, y) -> int:
    if field[y][x]:
        return 0

    field[y][x] = True

    if int(lines[y][x]) == 9:
        return 0

    val = 1

    if x > 0:
        val += basin(field, lines, x - 1, y)

    if y > 0:
        val += basin(field, lines, x, y - 1)
    
    if x < len(field[0]) - 1:
        val += basin(field, lines, x + 1, y)

    if y < len(field) - 1:
        val += basin(field, lines, x, y + 1)

    return val

def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 1

    basins = []

    height, width = len(lines), len(lines[0].strip())

    field = [[False for x in range(width)] for y in range(height)]
    
    for y in range(len(lines)):
        line = lines[y].strip()

        for x in range(len(line)):
            if field[y][x]:
                continue

            if int(lines[y][x]) == 9:
                field[y][x] = True
                continue

            basins.append(basin(field, lines, x, y))

    sortedBasins = sorted(basins)
    sortedBasins.reverse()

    for i in range(3):
        result *= sortedBasins[i]

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
