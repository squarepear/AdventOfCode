import math

def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    vals = [1, 2, 3, 4]

    missing = []
    
    for line in lines:
        stack = []
        err = False

        for char in line.strip():
            try:
                stack.append(closes[opens.index(char)])
                continue
            except:
                if char != stack.pop():
                    err = True
                    break

        if not err:
            missing.append(stack)

    scores = []

    for line in missing:
        score = 0

        line.reverse()

        for miss in line:
            score *= 5
            score += vals[closes.index(miss)]
        
        scores.append(score)

    scores.sort()

    result = scores[math.floor(len(scores) / 2)]

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
