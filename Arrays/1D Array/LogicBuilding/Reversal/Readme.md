# Reverse an Array

Reversing an array means changing the order of its elements so that the first element becomes the last, the second becomes the second last, and so on.

## Why Reverse an Array?

- Useful in algorithms that require processing data in reverse order.
- Common in problems involving palindromes, undo operations, or data structure manipulations.

## How to Reverse an Array

The most common approach is to swap elements from both ends moving towards the center.

**Example:**

Original array: `[1, 2, 3, 4, 5]`  
Reversed array: `[5, 4, 3, 2, 1]`

**Pseudocode:**
```
for i from 0 to n/2:
    swap(arr[i], arr[n-1-i])
```

## Further Reading

For detailed notes and explanations, [see this note](https://www.icloud.com/notes/0d5LTj0ZIFOz7FOcNaSKF2JIg#Reverse_an_Array:_-).