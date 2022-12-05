import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput()

function part1() {
    const stacksInput = input.split('\n\n')[0].split('\n')
    
    const stacks: String[][] = []

    for (let i = 0; i < (stacksInput[0].length + 1) / 4; i++) {
        const stack = []
        
        for (let j = 0; j < stacksInput.length - 1; j++) {
            const crate = stacksInput[j][ 1 + i * 4 ]

            if (crate === ' ')
                continue

            stack.push(crate)
        }

        stacks.push(stack)
    }
    
    input.split('\n\n')[1].trim().split('\n').forEach(line => {
        const [amount, from, to] = line.split(' ').map(x => parseInt(x)).filter(x => !isNaN(x))

        stacks[to - 1].unshift(...stacks[from - 1].splice(0, amount).reverse())
    })

    const output = stacks.map(stack => stack[0]).join('')

    saveOutputPart1(output)
}


function part2() {
    const stacksInput = input.split('\n\n')[0].split('\n')
    
    const stacks: String[][] = []

    for (let i = 0; i < (stacksInput[0].length + 1) / 4; i++) {
        const stack = []
        
        for (let j = 0; j < stacksInput.length - 1; j++) {
            const crate = stacksInput[j][ 1 + i * 4 ]

            if (crate === ' ')
                continue

            stack.push(crate)
        }

        stacks.push(stack)
    }
    
    input.split('\n\n')[1].trim().split('\n').forEach(line => {
        const [amount, from, to] = line.split(' ').map(x => parseInt(x)).filter(x => !isNaN(x))

        stacks[to - 1].unshift(...stacks[from - 1].splice(0, amount))
    })

    const output = stacks.map(stack => stack[0]).join('')

    saveOutputPart2(output)
}


part1()
part2()
