package main

import (
	"fmt"
	"strings"
)

func isPalindrome(str string) bool {
	// Convert the string to lowercase to handle case-insensitive palindromes
	str = strings.ToLower(str)

	// Iterate through the string and compare characters from both ends
	for i := 0; i < len(str)/2; i++ {
		if str[i] != str[len(str)-i-1] {
			return false
		}
	}
	return true
}

func main() {
	input := "racecar" // Change this to test different strings
	if isPalindrome(input) {
		fmt.Printf("%s is a palindrome.\n", input)
	} else {
		fmt.Printf("%s is not a palindrome.\n", input)
	}
}
