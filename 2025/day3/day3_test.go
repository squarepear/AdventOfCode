package day3_test

import (
	"bufio"
	"strings"
	"testing"

	"github.com/squarepear/aoc/2025/day3"
)

func TestParseInput(t *testing.T) {
	input := "1234\n5678\n9111\n"
	expected := []day3.Bank{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 1, 1, 1},
	}

	reader := bufio.NewReader(strings.NewReader(input))
	result, err := day3.ParseInput(reader)
	if err != nil {
		t.Fatalf("ParseInput returned error: %v", err)
	}

	if len(result) != len(expected) {
		t.Fatalf("ParseInput returned %d entries; want %d", len(result), len(expected))
	}

	for i, r := range result {
		if len(r) != len(expected[i]) {
			t.Fatalf("Entry %d has length %d; want %d", i, len(r), len(expected[i]))
		}
		for j, v := range r {
			if v != expected[i][j] {
				t.Errorf("Entry %d, value %d = %d; want %d", i, j, v, expected[i][j])
			}
		}
	}
}

func TestParseBank(t *testing.T) {
	tests := []struct {
		input    string
		expected day3.Bank
	}{
		{"1234", day3.Bank{1, 2, 3, 4}},
		{"5678", day3.Bank{5, 6, 7, 8}},
		{"9111", day3.Bank{9, 1, 1, 1}},
	}

	for _, test := range tests {
		result, err := day3.ParseBank(test.input)
		if err != nil {
			t.Errorf("ParseBank(%q) returned error: %v", test.input, err)
			continue
		}
		if len(result) != len(test.expected) {
			t.Errorf("ParseBank(%q) returned length %d; want %d", test.input, len(result), len(test.expected))
			continue
		}
		for i, v := range result {
			if v != test.expected[i] {
				t.Errorf("ParseBank(%q)[%d] = %d; want %d", test.input, i, v, test.expected[i])
			}
		}
	}
}

func TestSolvePart1(t *testing.T) {
	input := []day3.Bank{
		{9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1},
		{8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9},
		{2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8},
		{8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1},
	}
	expected := 357

	result := day3.SolvePart1(input)
	if result != expected {
		t.Errorf("SolvePart1() = %d; want %d", result, expected)
	}
}

func TestSolvePart2(t *testing.T) {
	input := []day3.Bank{
		{9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1},
		{8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9},
		{2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8},
		{8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1},
	}
	expected := 3121910778619

	result := day3.SolvePart2(input)
	if result != expected {
		t.Errorf("SolvePart2() = %d; want %d", result, expected)
	}
}
