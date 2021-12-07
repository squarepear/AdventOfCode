def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    data = lines[0].strip().split(',')

    val = (-1, 0)

    for x in range(2000):
        fuel = 0
        for i in range(len(data)):
            dist = abs(int(data[i]) - x)

            fuel += dist

        if fuel < val[1] or val[0] == -1:
            val = (x, fuel)

    result = val[1]

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
