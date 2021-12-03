def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0
    
    numBits = len(lines[0].strip())
    
    resultOxygen = lines
    resultCO2 = lines

    for i in range(numBits):
        counter = 0
        
        for j in range(len(resultOxygen)):
            line = resultOxygen[j].strip()

            if int(line[i]) == 1:
                counter += 1
            else:
                counter -= 1
        
        mostCommon = 0

        if counter >= 0:
            mostCommon = 1

        tempResult = []
        
        for j in range(len(resultOxygen)):
            line = resultOxygen[j].strip()

            if int(line[i]) == mostCommon:
                tempResult.append(line)

        resultOxygen = tempResult

        if len(resultOxygen) == 1:
            break

    for i in range(numBits):
        counter = 0
        
        for j in range(len(resultCO2)):
            line = resultCO2[j].strip()

            if int(line[i]) == 1:
                counter += 1
            else:
                counter -= 1
        
        leastCommon = 0

        if counter < 0:
            leastCommon = 1

        tempResult = []
        
        for j in range(len(resultCO2)):
            line = resultCO2[j].strip()

            if int(line[i]) == leastCommon:
                tempResult.append(line)

        resultCO2 = tempResult

        if len(resultCO2) == 1:
            break
    
    print(int(resultOxygen[0], 2), int(resultCO2[0], 2))
    result = int(resultOxygen[0], 2) * int(resultCO2[0], 2)

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
