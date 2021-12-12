import string

def step(node: str, start: str, end: str, nodes: dict, twice = False, path: list[str] = []):
    path.append(node)
    
    if node == end:
        print(path)
        return 1

    opts = nodes.get(node)

    val = 0

    for opt in opts:
        if not opt == start and (opt[0] in string.ascii_uppercase or (not opt in path or not twice)):
            val += step(opt, start, end, nodes, twice or (opt in path and not opt[0] in string.ascii_uppercase), path.copy())
    
    return val

def main():
    file = open("input.txt")

    lines = file.readlines()

    result = 0

    nodes = {}

    for line in lines:
        path = line.strip().split('-')

        node = nodes.setdefault(path[0], [])
        node.append(path[1])

        node = nodes.setdefault(path[1], [])
        node.append(path[0])

    result = step('start', 'start', 'end', nodes)

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
