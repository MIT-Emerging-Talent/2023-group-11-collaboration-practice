# Heap Sort Function

## Description

The `heap_sort` function sorts an input array of integers in ascending order using the Heap Sort algorithm.

## Behavior

- For an empty array, the result is an empty array.
- Returns the input array with a single element unchanged.
- Sorts the input array in ascending order.
- Sorts the input array in ascending order, even if the input is in decreasing order.
- Sorts the input array in ascending order.

## Parameters

- `arr` (List[int]): Input array of integers.

## Return Value

- `List[int]`: Sorted array in ascending order.

## Examples

```python
>>> heap_sort([1, 5, 2, 3, 8])
[1, 2, 3, 5, 8]

>>> heap_sort([])
[]

>>> heap_sort([1])
[1]
```
