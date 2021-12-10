def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    vals = [3, 57, 1197, 25137]

    errors = []
    
    for line in lines:
        stack = []

        for char in line.strip():
            try:
                stack.append(closes[opens.index(char)])
                continue
            except:
                if char != stack.pop():
                    errors += char
                    break

    for char in errors:
        result += vals[closes.index(char)]

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
