from ..utils import swap, partition, random_list_gen, is_sorted

def quick_sort(iterable, left=None, right=None):
	if iterable is None:
		return iterable

	if left is None:
		left = 0
	
	if right is None:
		right = len(iterable)-1

	if left < right:
		pivot = partition(iterable, left, right)
		quick_sort(iterable, left, pivot-1)
		quick_sort(iterable, pivot+1, right)

	return iterable

if __name__ == '__main__':
	test_cases = [100, 1000, 10000, 100000]
	for num in test_cases:
		l = random_list_gen(num)
		assert(is_sorted(quick_sort(l)) == True), "Unsorted list!"

	testListLong = [92, 25, 64, 39, 70, 98, 88, 46, 61, 20, 32, 82, 13, 97, 24, 42, 68, 66, 94, 65, 40, 37, 60, 2, 17, 44, 89, 37, 66, 93, 0, 55, 27, 7, 21, 93, 38, 58, 12, 8, 89, 50, 48, 44, 34, 18, 50, 57, 83, 16, 86, 34, 8, 54, 9, 14, 53, 62, 16, 67, 95, 94, 13, 89, 99, 55, 46, 20, 77, 97, 43, 36, 22, 39, 79, 26, 7, 85, 96, 37, 23, 73, 61, 93, 13, 43, 35, 97, 71, 43, 93, 28, 24, 86, 51, 9, 7, 19, 51, 19]
	assert(is_sorted(quick_sort(testListLong)) == True), "Unsorted list!"
