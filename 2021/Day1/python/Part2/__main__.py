def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    for i in range(0, len(lines) - 3):
        if (int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])) > (int(lines[i]) + int(lines[i+1]) + int(lines[i+2])):
            result += 1


    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()