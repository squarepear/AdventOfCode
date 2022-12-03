import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput()

const alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

function priority (char: string) {
    return alphabet.indexOf(char) + 1
}

function part1() {
    const output = input.trim().split('\n').map((line) => {
        const half = Math.floor(line.length / 2)

        const first = line.slice(0, half)
        const second = line.slice(half)

        const dup = first.split('').filter((a) => second.includes(a)).filter((a, i, arr) => arr.indexOf(a) === i)
        

        return dup.reduce((acc, cur) => acc + priority(cur), 0)
    }).reduce((a, b) => a + b, 0)

    saveOutputPart1(output)
}


function part2() {
    let inp = input.trim().split('\n')
    const groups = []

    for (var i = 0; i < inp.length; i+=3)
        groups.push(inp.slice(i, i+3))

    const output = groups.map((group) => {
        const first = group[0].split('')
        const second = group[1].split('')
        const third = group[2].split('')

        const dup = first.filter((a) => second.includes(a) && third.includes(a)).filter((a, i, arr) => arr.indexOf(a) === i)

        return dup.reduce((acc, cur) => acc + priority(cur), 0)
    }).reduce((a, b) => a + b, 0)

    saveOutputPart2(output)
}


part1()
part2()
