def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    points = []
    split = -1

    for i in range(len(lines)):
        line = lines[i].strip()

        if line == '':
            split = i + 1
            break

        x, y = line.split(',')

        points.append((int(x), int(y)))

    tempPoints = []

    for line in lines[split:split+1]:
        fold = line.split(' ')[2]
        dir, val = fold.strip().split('=')
        dir, val = 0 if dir == 'x' else 1, int(val)

        for point in points:
            if val == point[dir]:
                continue

            if point[dir] < val:
                if not point in tempPoints:
                    tempPoints.append(point)
                continue

            newPoint = None

            if dir == 0:
                newPoint = (2 * val - point[0], point[1])
            else:
                newPoint = (point[0], 2 * val - point[1])

            if not newPoint in tempPoints:
                tempPoints.append(newPoint)

        points, tempPoints = tempPoints, []

    result = len(points)

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
