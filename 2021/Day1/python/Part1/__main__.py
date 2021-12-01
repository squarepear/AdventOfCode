def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0
    for i in range(0, len(lines) - 1):
        if (int(lines[i+1])) > (int(lines[i])):
            result += 1


    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()