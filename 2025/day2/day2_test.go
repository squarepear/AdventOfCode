package day2_test

import (
	"bufio"
	"strings"
	"testing"

	"github.com/squarepear/aoc/2025/day2"
)

func TestParseInput(t *testing.T) {
	input := "1-3,5-7,10-15\n"
	expected := []day2.IDRange{
		{Start: 1, End: 3},
		{Start: 5, End: 7},
		{Start: 10, End: 15},
	}

	reader := bufio.NewReader(strings.NewReader(input))
	result, err := day2.ParseInput(reader)
	if err != nil {
		t.Fatalf("ParseInput returned error: %v", err)
	}

	if len(result) != len(expected) {
		t.Fatalf("ParseInput returned %d entries; want %d", len(result), len(expected))
	}

	for i, r := range result {
		if r != expected[i] {
			t.Errorf("Entry %d = %v; want %v", i, r, expected[i])
		}
	}
}

func TestParseRange(t *testing.T) {
	tests := []struct {
		input    string
		expected day2.IDRange
	}{
		{"1-3", day2.IDRange{Start: 1, End: 3}},
		{"5-7", day2.IDRange{Start: 5, End: 7}},
		{"10-15", day2.IDRange{Start: 10, End: 15}},
	}

	for _, test := range tests {
		result, err := day2.ParseRange(test.input)
		if err != nil {
			t.Errorf("ParseRange(%q) returned error: %v", test.input, err)
			continue
		}
		if result != test.expected {
			t.Errorf("ParseRange(%q) = %v; want %v", test.input, result, test.expected)
		}
	}
}

func TestParseRange_InvalidInput(t *testing.T) {
	var tests = []string{
		"3-1",
		"abc-def",
		"5-",
		"-10",
	}

	for _, input := range tests {
		_, err := day2.ParseRange(input)
		if err == nil {
			t.Errorf("ParseRange(%q) expected error but got nil", input)
		}
	}
}

func TestSolvePart1(t *testing.T) {
	input := []day2.IDRange{
		{Start: 11, End: 22},
		{Start: 95, End: 115},
		{Start: 998, End: 1012},
		{Start: 1188511880, End: 1188511890},
		{Start: 222220, End: 222224},
		{Start: 1698522, End: 1698528},
		{Start: 446443, End: 446449},
		{Start: 38593856, End: 38593862},
		{Start: 565653, End: 565659},
		{Start: 824824821, End: 824824827},
		{Start: 2121212118, End: 2121212124},
	}
	expected := 1227775554

	result := day2.SolvePart1(input)
	if result != expected {
		t.Errorf("SolvePart1() = %d; want %d", result, expected)
	}
}

func TestSolvePart2(t *testing.T) {
	input := []day2.IDRange{
		{Start: 11, End: 22},
		{Start: 95, End: 115},
		{Start: 998, End: 1012},
		{Start: 1188511880, End: 1188511890},
		{Start: 222220, End: 222224},
		{Start: 1698522, End: 1698528},
		{Start: 446443, End: 446449},
		{Start: 38593856, End: 38593862},
		{Start: 565653, End: 565659},
		{Start: 824824821, End: 824824827},
		{Start: 2121212118, End: 2121212124},
	}
	expected := 4174379265

	result := day2.SolvePart2(input)
	if result != expected {
		t.Errorf("SolvePart1() = %d; want %d", result, expected)
	}
}
