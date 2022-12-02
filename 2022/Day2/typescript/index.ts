import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput()

function part1() {
    const other = ['A', 'B', 'C']
    const you = ['X', 'Y', 'Z']

    const output = input.trim().split('\n').map((line) => {
        const otherIndex = other.indexOf(line[0])
        const youIndex = you.indexOf(line[2])

        let out = youIndex + 1

        if (youIndex == (otherIndex + 1) % 3)
            out += 6
        else if (youIndex == otherIndex)
            out += 3

        return out
    }).reduce((a, b) => a + b, 0)

    saveOutputPart1(output)
}


function part2() {
    const other = ['A', 'B', 'C']
    const you = ['X', 'Y', 'Z']

    const output = input.trim().split('\n').map((line) => {
        const result = you.indexOf(line[2])
        const otherIndex = other.indexOf(line[0])
        let youIndex = 0

        
        if (result == 0)
            youIndex = otherIndex - 1
        else if (result == 1)
            youIndex = otherIndex
        else if (result == 2)
            youIndex = otherIndex + 1
        
        youIndex = (youIndex + 3) % 3
        
        let out = youIndex + 1
        
        if (youIndex == (otherIndex + 1) % 3)
            out += 6
        else if (youIndex == otherIndex)
            out += 3

        return out
    }).reduce((a, b) => a + b, 0)

    saveOutputPart2(output)
}


part1()
part2()
