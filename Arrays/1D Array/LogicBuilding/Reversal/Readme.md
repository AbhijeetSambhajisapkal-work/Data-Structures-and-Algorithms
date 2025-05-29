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

---

## Rotating an Array by k Times

Rotating an array by k times means shifting each element of the array to the right (or left) by k positions. The elements that move past the end wrap around to the beginning.

### Why Rotate an Array?
- Used in cyclic scheduling, buffer management, and certain algorithmic problems.
- Helps in problems where the order of elements needs to be shifted while preserving the array's size.

### Example
Original array: `[1, 2, 3, 4, 5]`

Rotate right by 2:
Result: `[4, 5, 1, 2, 3]`

### Approaches
1. **Using Extra Space:**
   - Copy the last k elements to the front and the rest after them.
   - Time: O(n), Space: O(n)
2. **Rotate One by One:**
   - Shift elements one at a time, k times.
   - Time: O(n*k), Space: O(1)
3. **Reversal Algorithm (Efficient):**
   - Reverse the whole array.
   - Reverse the first k elements.
   - Reverse the remaining n-k elements.
   - Time: O(n), Space: O(1)

**Pseudocode (Reversal Algorithm):**
```
reverse(arr, 0, n-1)
reverse(arr, 0, k-1)
reverse(arr, k, n-1)
```

### Further Reading
For more on array rotation, see [this note](https://www.icloud.com/notes/0d5LTj0ZIFOz7FOcNaSKF2JIg#Rotate_an_Array:_-).