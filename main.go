package main

import "fmt"

func main() {
	unsortedSlice := []int{5, 3, 6, 2, 10}
	sortedSlice := SelectionSort(unsortedSlice)
	fmt.Println(sortedSlice)
}

func SelectionSort(mySlice []int) []int {
	returningSlice := make([]int, 0)
	smallest := 0
	startLen := len(mySlice)
	for i := 0; i < startLen; i++ {
		smallest = findSmallest(mySlice)
		returningSlice = append(returningSlice, mySlice[smallest])
		mySlice = append(mySlice[:smallest], mySlice[smallest+1:]...)
	}
	return returningSlice
}

func findSmallest(mySlice []int) int {
	smallest := mySlice[0]
	smallestIndex := 0
	for i, v := range mySlice {
		if v < smallest {
			smallest = v
			smallestIndex = i
		}
	}
	return smallestIndex
}
