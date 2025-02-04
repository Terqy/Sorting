import os
import random

nums = [random.randint(0, 1000000) for _ in range(1000000)]

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2

		leftArr = arr[:mid]
		rightArr = arr[mid:]

		mergeSort(leftArr)
		mergeSort(rightArr)

		i = j = k = 0
		while i < len(leftArr) and j < len(rightArr):
			if leftArr[i] < rightArr[j]:
				arr[k] = leftArr[i]
				i+=1
			else:
				arr[k] = rightArr[j]
				j+=1
			k+=1

		while i < len(leftArr):
			arr[k] = leftArr[i]
			i += 1
			k += 1

		while j < len(rightArr):
			arr[k] = rightArr[j]
			j += 1
			k += 1

	return arr

print(mergeSort(nums))