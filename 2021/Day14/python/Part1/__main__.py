def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0
    
    polymer = lines.pop(0).strip()
    lines.pop(0)

    pairs = {}

    for line in lines:
        pair, insert = line.split('->')
        pair, insert = pair.strip(), insert.strip()

        pairs.setdefault(pair, insert)

    for i in range(10):
        temp = list(polymer)
        offset = 1

        for j in range(len(polymer) - 1):
            insert = pairs.get(polymer[j:j+2])

            if insert != None:
                temp.insert(j + offset, insert)
                offset += 1

        polymer = ''.join(temp)

    indexes = []
    counts = []

    for el in polymer:
        if el in indexes:
            counts[indexes.index(el)] += 1
        else:
            indexes.append(el)
            counts.append(1)
    
    counts.sort()

    result = sum(counts[-1:]) - counts[0]

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
