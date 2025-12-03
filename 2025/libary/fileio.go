package libary

import (
	"bufio"
	"fmt"
	"os"
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
