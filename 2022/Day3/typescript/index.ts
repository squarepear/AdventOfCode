import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput()

function priority (char: string) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
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
    const output = input.trim().split('\n').reduce( (acc, cur, i) => {
            if (i % 3 === 0) acc.push([cur])
            else acc[acc.length - 1].push(cur)

            return acc
    }, []).map((group) => {
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
