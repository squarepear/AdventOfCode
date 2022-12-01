import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput().split('\n')

function part1() {
    let output = 0
    let current = 0

    for (const line of input) {
        if (line == '') {
            current = 0
            continue
        }

        current += parseInt(line, 10)

        if (current > output)
            output = current
    }

    saveOutputPart1(output)
}


function part2() {
    let output = 0
    let top = [0, 0, 0]
    let current = 0

    for (const line of input) {
        if (line != '') {
            current += parseInt(line, 10)
            continue
        }

        top.sort((a, b) => a - b)

        if (current > top[0])
            top[0] = current
        
        current = 0
    }

    output = top.reduce((a, b) => a + b, 0)

    saveOutputPart2(output)
}


part1()
part2()
