import { readFileSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'

let dir = ''
export function setDir(newDir: string) {
    dir = join(newDir, '../')
}

export function readInput(): string {
    const filePath = join(dir, 'input.txt')

    return readFileSync(filePath, 'utf8')
}

export function saveOutputPart1(output: any): void {
    const filePath = join(dir, 'output-part1.txt')

    writeFileSync(filePath, output.toString())
}

export function saveOutputPart2(output: any): void {
    const filePath = join(dir, 'output-part2.txt')

    writeFileSync(filePath, output.toString())
}
