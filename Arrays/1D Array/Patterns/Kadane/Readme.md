# Kadane's Algorithm

Kadane's Algorithm is an efficient method to find the **maximum sum subarray** in a one-dimensional array of numbers. It solves the "Maximum Subarray Problem" with a time complexity of O(n).

## Problem Statement

Given an array of integers (which may include negative numbers), find the contiguous subarray with the largest sum.

## Algorithm

1. Initialize two variables:
    - `max_so_far` = first element of the array
    - `max_ending_here` = first element of the array
2. Iterate through the array starting from the second element:
    - For each element `x`, set `max_ending_here = max(x, max_ending_here + x)`
    - Update `max_so_far = max(max_so_far, max_ending_here)`
3. `max_so_far` will contain the maximum subarray sum.

## Pseudocode

```python
def kadane(arr):
     max_so_far = arr[0]
     max_ending_here = arr[0]
     for x in arr[1:]:
          max_ending_here = max(x, max_ending_here + x)
          max_so_far = max(max_so_far, max_ending_here)
     return max_so_far
```

## Example

Input: `[−2, 1, −3, 4, −1, 2, 1, −5, 4]`  
Output: `6`  
Explanation: The subarray `[4, −1, 2, 1]` has the largest sum.

## Applications

- Financial analysis (maximum profit)
- Signal processing
- Dynamic programming problems

## References

- [Kadane's Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [LeetCode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [personal note](https://www.icloud.com/notes/0f5JMUYqXO5OTHLI9s4MWeteg#Kadane's_Algorithms-)
