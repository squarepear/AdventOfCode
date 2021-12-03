def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0
    
    numBits = len(lines[0].strip())

    result = 0
    counter = [0] * 12

    for i in range(len(lines)):
        line = lines[i]
        for j in range(numBits):
            if line[j] == "1":
                counter[j] += 1
            else:
                counter[j] -= 1

    epsilon = ''
    gamma = ''

    for bit in counter:
        if bit > 0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print(int(epsilon, 2), int(gamma, 2))
    result = int(epsilon, 2) * int(gamma, 2)

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
