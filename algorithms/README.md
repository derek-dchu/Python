Selection algorithms
====================
easiest: find the minimum or maximum, O(n), iterating through the list, keeping track of the running minimum or maximum.

hardest: finding the median, it necessarily takes n/2 storage.

sorting will benefits many selections, but is inefficient for selecting a single element.

quicksort
---------
find the  kth smallest with worst O(n^2), best O(n), average O(n). Note: it also partially sorts the data.

```
function partition(list, left, right, pivotIndex)
	pivotValue := list[pivotIndex]
	swap list[pivotIndex] and list[right]
	storeIndex := left
	for i from left to right-1
		if list[i] < pivotValue
			swap list[storeIndex] and list[i]
			increment storeIndex
	swap list[right] and list[storeIndex]
	return storeIndex
```

```
function select(list, left, right, n)
	if left = right
		return list[left]
	loop
		pivotIndex := left + Math.floor(Math.random() * (right - left + 1)
		pivotIndex := partition(list, left, right, pivotIndex)
		// The pivot is in its final sorted position
		if n = pivotIndex
			return list[n]
		else if n < pivotIndex
			right := pivotIndex - 1
		else
			left := pivotIndex + 1
```