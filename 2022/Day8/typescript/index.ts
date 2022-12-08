import { readInput, saveOutputPart1, saveOutputPart2, setDir } from '../../util/typescript'

setDir(import.meta.dir)
const input = readInput().trim()

function part1() {
    const grid = input.split('\n').map(line => line.split('').map(a => parseInt(a)))
    const visible = new Set<string>()

    // Get numbers that are higher than all other numbers towards an edge
    for (let y = 0; y < grid.length; y++) {
        let max = -1

        for (let x = 0; x < grid[y].length; x++) {
            if (grid[y][x] <= max)
                continue

            max = grid[y][x]
            visible.add(`${x},${y}`)
        }
    }

    for (let y = 0; y < grid.length; y++) {
        let max = -1

        for (let x = grid[y].length - 1; x >= 0; x--) {
            if (grid[y][x] <= max)
                continue

            max = grid[y][x]
            visible.add(`${x},${y}`)
        }
    }

    for (let x = 0; x < grid[0].length; x++) {
        let max = -1
        
        for (let y = 0; y < grid.length; y++) {
            if (grid[y][x] <= max)
                continue

            max = grid[y][x]
            visible.add(`${x},${y}`)
        }
    }

    for (let x = 0; x < grid[0].length; x++) {
        let max = -1

        for (let y = grid.length - 1; y >= 0; y--) {
            if (grid[y][x] <= max)
                continue

            max = grid[y][x]
            visible.add(`${x},${y}`)
        }
    }

    const output = new Array(...visible).length

    saveOutputPart1(output)
}


function part2() {
    const grid = input.split('\n').map(line => line.split('').map(a => parseInt(a)))

    const viewableGrid = new Array(grid.length).fill(0).map(() => new Array(grid[0].length).fill(0))

    // Get the viewable from each point on the grid
    for (let y = 0; y < grid.length; y++) {
        for (let x = 0; x < grid[y].length; x++) {
            const viewable = []

            // Get the viewable from each point on the grid
            let dir = 0
            for (let i = x - 1; i >= 0; i--) {
                dir += 1

                if (grid[y][i] >= grid[y][x])
                    break
            }
            viewable.push(dir)

            dir = 0
            for (let i = x + 1; i < grid[y].length; i++) {
                dir += 1

                if (grid[y][i] >= grid[y][x])
                    break
            }
            viewable.push(dir)

            dir = 0
            for (let i = y - 1; i >= 0; i--) {
                dir += 1

                if (grid[i][x] >= grid[y][x])
                    break
            }
            viewable.push(dir)

            dir = 0
            for (let i = y + 1; i < grid.length; i++) {
                dir += 1

                if (grid[i][x] >= grid[y][x])
                    break
            }
            viewable.push(dir)
            

            viewableGrid[y][x] = viewable.reduce((acc, val) => acc * val, 1)
        }
    }

    // Get the largest value in the viewable grid
    const output = viewableGrid.reduce((acc, row) => Math.max(acc, ...row), 0)
    
    saveOutputPart2(output)
}


part1()
part2()
