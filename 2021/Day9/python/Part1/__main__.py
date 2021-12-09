def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    lows = []

    height, width = len(lines), len(lines[0].strip())
    
    for y in range(len(lines)):
        line = lines[y].strip()

        for x in range(len(line)):
            val = int(lines[y][x])

            if val == 9:
                continue

            if x > 0 and val > int(lines[y][x - 1]):
                continue

            if y > 0 and val > int(lines[y - 1][x]):
                continue
            
            if x < width - 1 and val > int(lines[y][x + 1]):
                continue

            if y < height - 1 and val > int(lines[y + 1][x]):
                continue

            lows.append((x, y, val))
    
    for low in lows:
        result += low[2] + 1

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
