import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput()

function part1() {
    let output = 0

    const you = ['X', 'Y', 'Z']
    const them = ['A', 'B', 'C']

    input.trim().split('\n').forEach((line) => {
        let move = line.split(' ')

        let youIndex = you.indexOf(move[1])
        let themIndex = them.indexOf(move[0])

        output += youIndex + 1

        if (youIndex == themIndex + 1 || (youIndex == 0 && themIndex == 2))
            output += 6
        else if (youIndex == themIndex)
            output += 3
    })

    saveOutputPart1(output)
}


function part2() {
    let output = 0

    const you = ['X', 'Y', 'Z']
    const them = ['A', 'B', 'C']

    input.trim().split('\n').forEach((line) => {
        let move = line.split(' ')

        let result = you.indexOf(move[1])
        let themIndex = them.indexOf(move[0])
        let youIndex = 0

        if (result == 0)
            youIndex = themIndex - 1
        else if (result == 1)
            youIndex = themIndex
        else if (result == 2)
            youIndex = themIndex + 1

        youIndex = (youIndex + 3) % 3

        output += youIndex + 1

        if (youIndex == themIndex + 1 || (youIndex == 0 && themIndex == 2))
            output += 6
        else if (youIndex == themIndex)
            output += 3
    })

    saveOutputPart2(output)
}


part1()
part2()
