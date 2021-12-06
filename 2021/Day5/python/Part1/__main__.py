def main():
    file = open("input.txt")

    lines = file.readlines()

    points = {}

    result = 0


    for line in lines:
        coordIn = line.strip().split(' ')

        one = coordIn[0].split(',')
        two = coordIn[2].split(',')


        x = int(one[0])
        y = int(one[1])

        if (one[0] == two[0]):
            span = [int(one[1]), int(two[1])]
            span.sort()
            for y in range(span[0], span[1] + 1):
                points.setdefault(f"{x},{y}", 0)
                points[f"{x},{y}"] += 1

        if (one[1] == two[1]):
            span = [int(one[0]), int(two[0])]
            span.sort()
            for x in range(span[0], span[1] + 1):
                points.setdefault(f"{x},{y}", 0)
                points[f"{x},{y}"] += 1


    result = len(dict(filter(lambda item: item[1] >= 2, points.items())))

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
