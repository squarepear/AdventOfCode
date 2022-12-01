import { readInput, saveOutputPart1, saveOutputPart2 } from '../../util/typescript';

function part1() {
    const input = readInput();
    let output = 0;
    let current = 0

    for (const line of input) {
        if (line == '') {
            current = 0;
            continue
        }

        current += parseInt(line, 10);

        if (current > output)
            output = current;
    }

    saveOutputPart1(output);
}


function part2() {
    const input = readInput();
    let output = 0;
    let top = [0, 0, 0]
    let current = 0

    for (const line of input) {
        if (line != '') {
            current += parseInt(line, 10);

            continue
        }

        top.sort((a, b) => a - b);

        if (current > top[0]) {
            top[0] = current;
        } else if (current > top[1]) {
            top[1] = current;
        } else if (current > top[2]) {
            top[2] = current;
        }
        
        current = 0;
    }

    saveOutputPart2(top[0] + top[1] + top[2]);
}

part1();
part2();
