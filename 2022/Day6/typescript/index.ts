import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput().trim()

function part1() {
    const size = 4
    let output = 0
    
    for (let i = size - 1; i < input.length; i++) {
        if (!(new Set(input.slice(i - size, i)).size === size))
            continue
        
        output = i
        break
    }

    saveOutputPart1(output)
}


function part2() {
    const size = 14
    let output = 0

    for (let i = size - 1; i < input.length; i++) {
        if (!(new Set(input.slice(i - size, i)).size === size))
            continue
        
        output = i
        break
    }

    saveOutputPart2(output)
}


part1()
part2()
