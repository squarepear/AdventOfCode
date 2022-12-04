import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput()

function part1() {
    const output = input.trim().split('\n').map((line) => {
        const [first, second] = line.split(',').map((task) => {
            const [start, end] = task.split('-').map((a) => parseInt(a))
            const tasks = []

            for (let i = start; i <= end; i++)
                tasks.push(i)

            return tasks
        })

        const unique = new Set([...first, ...second])

        if (unique.size === first.length || unique.size === second.length)
            return 1
        
        return 0
    }).reduce((a, b) => a + b, 0)

    saveOutputPart1(output)
}


function part2() {
    const output = input.trim().split('\n').map((line) => {
        const [first, second] = line.split(',').map((task) => {
            const [start, end] = task.split('-').map((a) => parseInt(a))
            const tasks = []

            for (let i = start; i <= end; i++)
                tasks.push(i)

            return tasks
        })

        const unique = new Set([...first, ...second])

        if (unique.size !== first.length + second.length)
            return 1
        
        return 0
    }).reduce((a, b) => a + b, 0)

    saveOutputPart2(output)
}


part1()
part2()
