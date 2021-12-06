def main():
    file = open("input.txt")

    lines = file.readlines()

    points = {}

    result = 0


    for line in lines:
        coordIn = line.strip().split('->')

        [x1, y1] = [int(i) for i in coordIn[0].strip().split(',')]
        [x2, y2] = [int(i) for i in coordIn[1].strip().split(',')]



        if x1 == x2:
            x = x1
            minY = min(y1, y2)
            maxY = max(y1, y2)

            for y in range(minY, maxY + 1):
                points.setdefault(f"{x},{y}", 0)
                points[f"{x},{y}"] += 1

        else:
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1

            minX = min(x1, x2)
            maxX = max(x1, x2)

            for x in range(minX, maxX + 1):
                y = round(m * x + b)

                points.setdefault(f"{x},{y}", 0)
                points[f"{x},{y}"] += 1

    result = len(dict(filter(lambda item: item[1] >= 2, points.items())))

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
