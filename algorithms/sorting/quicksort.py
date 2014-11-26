from random import randint

def test(pivot, left, right):
	print "p: {} | l: {} | r: {}".format(pivot, left, right)

def swap(arr, i1, i2):
	arr[i1], arr[i2] = arr[i2], arr[i1]

def partition(arr, first, last):
	pivot = first + int((last - first) / 2)
	swap(arr, first, pivot)
	left = first + 1
	right = last
	while True:
		while arr[left] < arr[first]:
			if left == last:
				break
			left += 1

		while arr[right] >= arr[first]:
			if right == first:
				break
			right -= 1

		if left >= right:
			break

		swap(arr, left, right)
		left += 1
		right -= 1

	swap(arr, first, right)
	return right

def quick_sort(arr, first=None, last=None):
	if arr is None:
		return arr

	if first is None:
		first = 0

	if last is None:
		last = len(arr)-1

	if first < last:
		pivot = partition(arr, first, last)
		quick_sort(arr, first, pivot-1)
		quick_sort(arr, pivot+1, last)

	return arr

def random_arr_gen(num):
	arr = []
	for i in range(0, num):
		arr.append(randint(0, num))
	return arr

def is_sorted(arr):
	for i in range(1, len(arr)):
		if (arr[i-1] > arr[i]):
			return False
	return True

## test section
test_cases = [100, 1000, 10000, 100000]
for num in test_cases:
	arr = random_arr_gen(num)
	assert(is_sorted(quick_sort(arr)) == True), "Unsorted Array!"

testListLong = [92, 25, 64, 39, 70, 98, 88, 46, 61, 20, 32, 82, 13, 97, 24, 42, 68, 66, 94, 65, 40, 37, 60, 2, 17, 44, 89, 37, 66, 93, 0, 55, 27, 7, 21, 93, 38, 58, 12, 8, 89, 50, 48, 44, 34, 18, 50, 57, 83, 16, 86, 34, 8, 54, 9, 14, 53, 62, 16, 67, 95, 94, 13, 89, 99, 55, 46, 20, 77, 97, 43, 36, 22, 39, 79, 26, 7, 85, 96, 37, 23, 73, 61, 93, 13, 43, 35, 97, 71, 43, 93, 28, 24, 86, 51, 9, 7, 19, 51, 19]
assert(is_sorted(quick_sort(testListLong)) == True), "Unsorted Array!"
