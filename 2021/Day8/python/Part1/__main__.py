def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    tests = []

    for line in lines:
        test = line.split('|')


        tests.append((test[0].strip().split(' '), test[1].strip().split(' ')))

    for test in tests:
        for digit in test[1]:
            length = len(digit)
            if length == 2 or length == 3 or length == 4 or length == 7:
                result += 1

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
