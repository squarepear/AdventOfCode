def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    data = lines[0].strip().split(',')

    for i in range(80):
        for j in range(len(data)):
            if int(data[j]) == 0:
                data.append(8)
                data[j] = int(6)
            else:
                data[j] = int(data[j]) - 1

    result = len(data)

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
