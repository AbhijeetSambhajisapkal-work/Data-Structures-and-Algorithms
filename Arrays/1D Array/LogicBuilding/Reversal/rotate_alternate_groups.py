## Rotate Alternate Groups in an Array

# **Problem Statement:**  
# Given an array of size `n` and a positive integer `k`, rotate every alternate group of `k` elements in the array to the right by one position. 
# The first group of `k` elements should be rotated, the next group of `k` elements should be left as is, 
# the third group should be rotated, and so on. If the last group has fewer than `k` elements, 
# rotate it as well if it is an alternate group to be rotated.

# **Example:**  
# Input:  
# `arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`, `k = 3`

# Output:  
# `[3, 1, 2, 4, 5, 6, 9, 7, 8, 10, 11]`

# **Explanation:**  
# - First group `[1, 2, 3]` → rotate right → `[3, 1, 2]`
# - Second group `[4, 5, 6]` → unchanged
# - Third group `[7, 8, 9]` → rotate right → `[9, 7, 8]`
# - Fourth group `[10, 11]` → unchanged

def rotate_alternate_groups(arr, k):
    n = len(arr)
    for i in range(0, n, k):
        group_idx = (i // k)
        if group_idx % 2 == 0:
            # Rotate this group to the right by 1
            end = min(i + k, n)
            if end - i > 1:
                last = arr[end - 1]
                for j in range(end - 1, i, -1):
                    arr[j] = arr[j - 1]
                arr[i] = last
    return arr


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_alternate_groups_other(A, k):
    n = len(A)
    for i in range(0, n, k):
        group_idx = (i // k)
        if group_idx % 2 == 0:
            end = min(i + k, n)
            if end - i > 1:
                reverse(A, i, end - 1)
                reverse(A, i, i)
                reverse(A, i + 1, end - 1)
    return A


# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    k = 3
    rotate_alternate_groups(arr, k)
    print(arr)  # Output: [3, 1, 2, 4, 5, 6, 9, 7, 8, 10, 11]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    rotate_alternate_groups_other(arr2, k)
    print(arr2)  # Output: [3, 1, 2, 4, 5, 6, 9, 7, 8, 10, 11]
