package libary

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const InputFile = "day%d/input.txt"

func LoadInput(day int) (*bufio.Reader, error) {
	filename := fmt.Sprintf(InputFile, day)
	file, err := os.Open(filename)
	if err != nil {
		return nil, fmt.Errorf("failed to open input file %s: %w", filename, err)
	}

	return bufio.NewReader(file), nil
}

func ScanComma(data []byte, atEOF bool) (advance int, token []byte, err error) {
	if atEOF && len(data) == 0 {
		return 0, nil, nil
	}

	if i := strings.Index(string(data), ","); i >= 0 {
		// We have a full comma-terminated line.
		return i + 1, data[0:i], nil
	}

	if atEOF {
		// Return the final token.
		return len(data), data, nil
	}

	// Request more data.
	return 0, nil, nil
}
