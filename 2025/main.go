package main

import (
	"fmt"
	"os"
)

var Days = map[int]func() error{}

func main() {
	args := os.Args
	if len(args) < 2 {
		fmt.Println("Please provide the day number to execute")
		return
	}

	day := 0
	_, err := fmt.Sscanf(args[1], "%d", &day)
	if err != nil {
		fmt.Println("Invalid day number")
		return
	}

	if execute, exists := Days[day]; exists {
		err := execute()
		if err != nil {
			fmt.Printf("Error executing day %d: %v\n", day, err)
		}
	} else {
		fmt.Println("Day not implemented")
	}
}
