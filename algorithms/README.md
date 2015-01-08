Selection algorithms
====================
easiest: find the minimum or maximum, O(n), iterating through the list, keeping track of the running minimum or maximum.

hardest: finding the median, it necessarily takes n/2 storage.

sorting will benefits many selections, but is inefficient for selecting a single element.

quickselect
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
function quickselect(list, left, right, n)
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

median-of-medians
-----------------
Compute an approximate median, which is guaranteed to be between the 30th and 70th percentiles with worst O(n), best O(n).

```
function medianOfMedians(list, left, right)
    // divide the list into groups of five elements
    numMedians = ceil((right - left) / 5)
    for i from 0 to numMedians
        subLeft := left + i*5
        subRight := subLeft + 4
        if (subRight > right) subRight := right
        // get the median using quick select
        medianIndex := quickselectIndex(list, subLeft, subRight, (subRight - subLeft) / 2)
        // move the median to a contiguous block at the beginning of the list
        swap list[left+i] and list[medianIndex]
    // select the median from the contiguous block
    medianOfMediansIndex = quickselectIndex(list, left, left + numMedian - 1, numMedian / 2)
    return list[medianOfMediansIndex]
```