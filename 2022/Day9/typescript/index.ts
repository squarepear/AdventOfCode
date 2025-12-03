import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput().trim()

type Knot = { x: number, y: number }

function physics (head: Knot, tail: Knot): Array<string> {
    const visited = new Set<string>()

    if (Math.abs(head.x - tail.x) > 1 && head.y !== tail.y || Math.abs(head.y - tail.y) > 1 && head.x !== tail.x) {
        visited.add(`${tail.x},${tail.y}`)

        if (tail.x < head.x)
            tail.x++
        else if (tail.x > head.x)
            tail.x--
        
        if (tail.y < head.y)
            tail.y++
        else if (tail.y > head.y)
            tail.y--
    }
    
    if (head.y > tail.y)
        while (tail.y + 1 < head.y)
            visited.add(`${tail.x},${tail.y++}`)
    else if (head.y < tail.y)
        while (tail.y - 1 > head.y)
            visited.add(`${tail.x},${tail.y--}`)
    else if (head.x > tail.x)
        while (tail.x + 1 < head.x)
            visited.add(`${tail.x++},${tail.y}`)
    else if (head.x < tail.x)
        while (tail.x - 1 > head.x)
            visited.add(`${tail.x--},${tail.y}`)

    return new Array(...visited)
}

function part1() {
    const visited = new Set<string>()

    const head = { x: 0, y: 0 }
    const tail = { x: 0, y: 0 }

    input.split('\n').forEach(line => {
        const [dir, steps] = line.split(' ')

        switch (dir) {
            case 'R':
                head.x += parseInt(steps)
                break
            case 'L':
                head.x -= parseInt(steps)
                break
            case 'U':
                head.y += parseInt(steps)
                break
            case 'D':
                head.y -= parseInt(steps)
                break
        }

        physics(head, tail).forEach(a => visited.add(a))
    })

    visited.add(`${tail.x},${tail.y}`)

    const output = visited.size

    saveOutputPart1(output)
}


function part2() {
    const length = 10
    const visited = new Set<string>()

    const knots = new Array(length).fill(0).map((_, i) => ({ x: 0, y: 0 }))

    input.split('\n').forEach(line => {
        const [dir, steps] = line.split(' ')

        switch (dir) {
            case 'R':
                knots[0].x += parseInt(steps)
                break
            case 'L':
                knots[0].x -= parseInt(steps)
                break
            case 'U':
                knots[0].y += parseInt(steps)
                break
            case 'D':
                knots[0].y -= parseInt(steps)
                break
        }

        for (let i = 1; i < knots.length; i++) {
            const head = knots[i - 1]
            const tail = knots[i]

            const knotVisited = physics(head, tail)

            if (i === knots.length - 1)
                knotVisited.forEach(a => visited.add(a))
        }
    })

    visited.add(`${knots[length - 1].x},${knots[length - 1].y}`)

    const output = new Array(...visited).join('\n')
    
    saveOutputPart2(output)
}


part1()
part2()
