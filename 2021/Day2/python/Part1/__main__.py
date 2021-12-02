def main():
    file = open("input.txt")

    lines = file.readlines()

    x, y = 0, 0

    for i in range(0, len(lines)):
        command = lines[i].split(" ")

        if (command[0] == "forward"):
            x += int(command[1])
        elif (command[0] == "up"):
            y -= int(command[1])
        elif (command[0] == "down"):
            y += int(command[1])

    print(str([x, y]))

    out = open("output-part1.txt", "w")
    out.write(str(x * y))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
