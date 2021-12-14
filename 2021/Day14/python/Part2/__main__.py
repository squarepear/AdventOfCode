def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0
    
    polymer = lines.pop(0).strip()
    lines.pop(0)

    pairs = {}
    counts = {}

    for line in lines:
        pair, insert = line.split('->')
        pair, insert = pair.strip(), insert.strip()

        pairs.setdefault(pair, insert)
    
    for i in range(0, len(polymer) - 1):
        pair = polymer[i:i+2]

        counts.setdefault(pair, 0)
        counts[pair] += 1

    for i in range(40):
        temp = {}

        for pair in counts.keys():
            insert = pairs[pair]

            newPairs = (pair[0] + insert, insert + pair[1])

            temp.setdefault(newPairs[0], 0)
            temp.setdefault(newPairs[1], 0)

            temp[newPairs[0]] += counts[pair]
            temp[newPairs[1]] += counts[pair]

        counts = temp

    chars = {}

    first = list(counts.keys())[0]
    chars.setdefault(first[0], 0)
    chars[first[0]] += counts[first]

    for pair in counts.keys():
        chars.setdefault(pair[1], 0)

        chars[pair[1]] += counts[pair]

    chars = list(chars.values())

    chars.sort()

    result = chars[-1:][0] - chars[0]

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
