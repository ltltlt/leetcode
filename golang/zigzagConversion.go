// pass, beat 100% go submissions
// this problem is easy, just find some patterns first
package main

import (
	"bytes"
	"fmt"
)

func convert(s string, numRows int) string {
	var buffer bytes.Buffer
	for i := 0; i < numRows; i++ {
		first := i
		step1, step2 := 2*(numRows-i)-2, 2*i
		if step1 == 0 {
			step1 = step2
		} else if step2 == 0 {
			step2 = step1
		}
		if step1 == 0 { // when numRows equals to 1
			step1, step2 = 1, 1
		}
		for j := first; ; {
			if j < len(s) {
				buffer.WriteByte(s[j])
			} else {
				break
			}
			j += step1
			if j < len(s) {
				buffer.WriteByte(s[j])
			} else {
				break
			}
			j += step2
		}
	}
	return buffer.String()
}

func main() {
	fmt.Println(convert("AB", 2))
}
