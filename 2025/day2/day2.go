package day2

import (
	"bufio"
	"fmt"
	"strconv"

	"github.com/squarepear/aoc/2025/libary"
)

type IDRange struct {
	Start int
	End   int
}

func Execute() error {
	// Load input file
	input, err := libary.LoadInput(2)
	if err != nil {
		return err
	}

	// Parse input data
	data, err := ParseInput(input)
	if err != nil {
		return err
	}

	fmt.Printf("Loaded %d entries from input\n", len(data))

	// Solve part 1
	part1Result := SolvePart1(data)
	fmt.Printf("Part 1 Result: %d\n", part1Result)

	// Solve part 2
	part2Result := SolvePart2(data)
	fmt.Printf("Part 2 Result: %d\n", part2Result)

	return nil
}

func ParseInput(reader *bufio.Reader) ([]IDRange, error) {
	scanner := bufio.NewScanner(reader)
	var inputData []IDRange

	scanner.Split(libary.ScanComma)
	for scanner.Scan() {
		input := scanner.Text()
		value, err := ParseRange(input)
		if err != nil {
			return nil, err
		}

		inputData = append(inputData, value)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return inputData, nil
}

// Range format: "X-Y" where X and Y are integers
func ParseRange(input string) (IDRange, error) {
	var idRange IDRange

	_, err := fmt.Sscanf(input, "%d-%d", &idRange.Start, &idRange.End)
	if err != nil {
		return IDRange{}, err
	}

	if idRange.End < idRange.Start {
		return IDRange{}, fmt.Errorf("invalid range: end %d is less than start %d", idRange.End, idRange.Start)
	}

	return idRange, nil
}

func SolvePart1(data []IDRange) int {
	solution := 0

	for _, r := range data {
		for i := r.Start; i <= r.End; i++ {
			id := strconv.Itoa(i)

			if len(id)%2 == 1 {
				continue
			}

			mid := len(id) / 2
			firstHalf := id[:mid]
			secondHalf := id[mid:]

			if firstHalf == secondHalf {
				solution += i
			}
		}
	}

	return solution
}

func SolvePart2(data []IDRange) int {
	solution := 0

	for _, r := range data {
		for i := r.Start; i <= r.End; i++ {
			id := strconv.Itoa(i)

			for size := 1; size <= len(id)/2; size++ {
				if len(id)%size != 0 {
					continue
				}

				pattern := id[:size]
				matches := true

				for j := size; j < len(id); j += size {
					if id[j:j+size] != pattern {
						matches = false
						break
					}
				}

				if matches {
					solution += i
					break
				}
			}
		}
	}
	return solution
}
