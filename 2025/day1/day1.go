package day1

import (
	"bufio"
	"fmt"

	"github.com/squarepear/aoc/2025/libary"
)

func Execute() error {
	// Load input file
	input, err := libary.LoadInput(1)
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

func ParseInput(reader *bufio.Reader) ([]int, error) {
	scanner := bufio.NewScanner(reader)
	var inputData []int

	for scanner.Scan() {
		line := scanner.Text()
		value, err := ParseLine(line)
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

// Line format: L or R followed by integer distance, e.g. "R2", "L33"
func ParseLine(line string) (int, error) {
	var direction rune
	var distance int
	_, err := fmt.Sscanf(line, "%c%d", &direction, &distance)
	if err != nil {
		return 0, err
	}

	if distance < 0 {
		return 0, fmt.Errorf("distance cannot be negative: %d", distance)
	}

	// Convert to a signed integer based on direction
	switch direction {
	case 'L':
		return -distance, nil
	case 'R':
		return distance, nil
	}

	return 0, fmt.Errorf("invalid direction: %c", direction)
}

func SolvePart1(data []int) int {
	currentPosition := 50
	solution := 0

	for _, move := range data {
		currentPosition += move % 100

		currentPosition = (currentPosition + 100) % 100

		if currentPosition == 0 {
			solution++
		}
	}

	return solution
}

func SolvePart2(data []int) int {
	currentPosition := 50
	solution := 0

	for _, move := range data {
		absMove := max(move, -move)
		solution += absMove / 100

		if move > 0 {
			currentPosition += absMove % 100
		} else {
			currentPosition -= absMove % 100
		}

		if (currentPosition < 0 || currentPosition > 100) && (currentPosition-move)%100 != 0 {
			solution++
		}

		currentPosition = (currentPosition + 100) % 100

		if currentPosition == 0 && move%100 != 0 {
			solution++
		}
	}

	return solution
}
