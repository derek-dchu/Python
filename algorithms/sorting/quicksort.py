from random import randint

def test(pivot, left, right):
	print "p: {} | l: {} | r: {}".format(pivot, left, right)

def swap(arr, i1, i2):
	arr[i1], arr[i2] = arr[i2], arr[i1]

def partition(arr, first, last):
	pivot = int((first + last) / 2)
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

