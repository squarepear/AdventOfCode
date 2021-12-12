import string

def step(node: str, end: str, nodes: dict, path: list[str] = []):
    path.append(node)

    if node == end:
        return 1

    opts = nodes.get(node)

    val = 0

    for opt in opts:
        if opt[0] in string.ascii_uppercase or not opt in path:
            val += step(opt, end, nodes, path.copy())
    
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
    
    result = step('start', 'end', nodes)

    out = open("output-part1.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
