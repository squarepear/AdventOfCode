package day1_test

import (
	"bufio"
	"strings"
	"testing"

	"github.com/squarepear/aoc/2025/day1"
)

func TestParseInput(t *testing.T) {
	inputData := "R2\nL3\nR0\nL5\n"
	expected := []int{2, -3, 0, -5}

	reader := bufio.NewReader(strings.NewReader(inputData))
	result, err := day1.ParseInput(reader)
	if err != nil {
		t.Fatalf("ParseInput returned error: %v", err)
	}

	if len(result) != len(expected) {
		t.Fatalf("ParseInput returned %d entries; want %d", len(result), len(expected))
	}

	for i, v := range result {
		if v != expected[i] {
			t.Errorf("ParseInput entry %d = %d; want %d", i, v, expected[i])
		}
	}
}

func TestParseLine(t *testing.T) {
	var tests = []struct {
		input    string
		expected int
	}{
		{"R2", 2},
		{"L33", -33},
		{"R0", 0},
		{"L0", 0},
		{"R999", 999},
		{"L100", -100},
	}

	for _, test := range tests {
		result, err := day1.ParseLine(test.input)
		if err != nil {
			t.Errorf("ParseLine(%q) returned error: %v", test.input, err)
		}
		if result != test.expected {
			t.Errorf("ParseLine(%q) = %d; want %d", test.input, result, test.expected)
		}
	}
}

func TestParseLine_InvalidInput(t *testing.T) {
	var tests = []string{
		"X2",
		"R-3",
		"Labc",
		"",
		"123",
	}

	for _, input := range tests {
		_, err := day1.ParseLine(input)
		if err == nil {
			t.Errorf("ParseLine(%q) expected error, got nil", input)
		}
	}
}

func TestSolvePart1(t *testing.T) {
	data := []int{-68, -30, 48, -5, 60, -55, -1, -99, 14, -82}
	expected := 3
	result := day1.SolvePart1(data)

	if result != expected {
		t.Errorf("SolvePart1() = %d; want %d", result, expected)
	}
}

func TestSolvePart2(t *testing.T) {
	tests := []struct {
		name     string
		data     []int
		expected int
	}{
		{
			name:     "No crossings",
			data:     []int{10, -20, 30},
			expected: 0,
		},
		{
			name:     "Single crossing",
			data:     []int{60, 50},
			expected: 1,
		},
		{
			name:     "Multiple crossings",
			data:     []int{-150, 250, -300},
			expected: 7,
		},
		{
			name:     "Test Input Data",
			data:     []int{-68, -30, 48, -5, 60, -55, -1, -99, 14, -82},
			expected: 6,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := day1.SolvePart2(tt.data)
			if result != tt.expected {
				t.Errorf("SolvePart2() = %d; want %d", result, tt.expected)
			}
		})
	}
}
