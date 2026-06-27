package main

func TowSum(nums []int, target int) [2]int {

	var obj = map[int]int{}

	for ind, no := range nums {
		remain := target - no
		if i, ok := obj[remain]; ok == true {
			return [2]int{ind, i}
		}
		obj[no] = ind
	}

	return [2]int{}
}
