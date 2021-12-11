def flash(octopi, flashed, x, y, base=True):
    if not base:
        octopi[y][x] += 1

    if flashed[y][x] or octopi[y][x] <= 9:
        return 0
    
    flashed[y][x] = True
    val = 1

    if x > 0:
        val += flash(octopi, flashed, x - 1, y, False)
    if y > 0:
        val += flash(octopi, flashed, x, y - 1, False)
    if x < len(octopi[y]) - 1:
        val += flash(octopi, flashed, x + 1, y, False)
    if y < len(octopi) - 1:
        val += flash(octopi, flashed, x, y + 1, False)
    if x > 0 and y > 0:
        val += flash(octopi, flashed, x - 1, y - 1, False)
    if x < len(octopi[y]) - 1 and y > 0:
        val += flash(octopi, flashed, x + 1, y - 1, False)
    if x > 0 and y < len(octopi) - 1:
        val += flash(octopi, flashed, x - 1, y + 1, False)
    if x < len(octopi[y]) - 1 and y < len(octopi) - 1:
        val += flash(octopi, flashed, x + 1, y + 1, False)

    return val

def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    octopi = []

    for line in lines:
        row = []

        for val in line.strip():
            row.append(int(val))
        
        octopi.append(row)

    i = 1
    while True:
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                octopi[y][x] += 1
        
        flashed = [[False for x in range(len(octopi[y]))] for y in range(len(octopi))]
        allFlash = True

        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                flash(octopi, flashed, x, y)

        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                if flashed[y][x]:
                    octopi[y][x] = 0
                else:
                    allFlash = False
        
        if allFlash:
            result = i
            break

        i += 1

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
