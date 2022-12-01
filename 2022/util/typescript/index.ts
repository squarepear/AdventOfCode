import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

export function readInput(): string[] {
    const filePath = join(import.meta.dir, '../../Day1/input.txt');

    return readFileSync(filePath, 'utf8').split('\n');
}

export function readInputAsNumbers(): number[] {
    return readInput().map((line) => parseInt(line, 10));
}

export function saveOutputPart1(output: any): void {
    const filePath = join(import.meta.dir, '../../Day1/output-part1.txt');

    writeFileSync(filePath, output.toString());
}

export function saveOutputPart2(output: any): void {
    const filePath = join(import.meta.dir, '../../Day1/output-part2.txt');

    writeFileSync(filePath, output.toString());
}
