package day3

import (
	"bufio"
	"fmt"
	"math"
	"strconv"

	"github.com/squarepear/aoc/2025/libary"
)

type Bank []int

func Execute() error {
	// Load input file
	input, err := libary.LoadInput(3)
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

func ParseInput(reader *bufio.Reader) ([]Bank, error) {
	scanner := bufio.NewScanner(reader)
	var inputData []Bank

	for scanner.Scan() {
		line := scanner.Text()
		value, err := ParseBank(line)
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

// Bank format: "ABCD..." where A, B, C, D, ... are integers representing battery capacities
func ParseBank(input string) (Bank, error) {
	var bank Bank

	for _, ch := range input {
		capacity, err := strconv.Atoi(string(ch))
		if err != nil {
			return nil, fmt.Errorf("invalid battery capacity %q: %w", string(ch), err)
		}
		bank = append(bank, capacity)
	}

	return bank, nil
}

func SolvePart1(data []Bank) int {
	solution := 0

	for _, bank := range data {
		highTens, highOnes := 0, 0
		for i, battery := range bank {
			if battery > highTens && i < len(bank)-1 {
				highTens = battery
				highOnes = 0
				continue
			}

			if battery > highOnes {
				highOnes = battery
			}
		}

		solution += highTens*10 + highOnes
	}

	return solution
}

func SolvePart2(data []Bank) int {
	solution := 0
	size := 12

	for _, bank := range data {
		highs := make([]int, size)

		for i, battery := range bank {
			for j, high := range highs {
				if battery <= high || i > len(bank)-(size-j) {
					continue
				}

				highs[j] = battery

				for k := range highs[j+1:] {
					highs[j+k+1] = 0
				}

				break
			}
		}

		joltage := 0
		for i, high := range highs {
			joltage += high * int(math.Pow10((size - i - 1)))
		}

		solution += joltage
	}

	return solution
}
