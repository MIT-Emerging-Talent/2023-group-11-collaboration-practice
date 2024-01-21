# array_product Function Documentation

## Description

The `array_product` function takes a list of integers as input and returns an array where each element is equal to the product of all elements in the input array, excluding the current one.

## Behavior

- For an empty array, the result is an empty array.
- For an array with one element, the result is an array containing that element.
- Assumes input elements are integers starting from 1.

## Parameters

- `nums` (List[int]): Input array of integers.

## Return Value

- `List[int]`: Array where each element is the product of all elements in the input array, excluding the current one.

## Examples

```python
>>> array_product([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> array_product([])
[]
  
>>> array_product([1])
[1]
