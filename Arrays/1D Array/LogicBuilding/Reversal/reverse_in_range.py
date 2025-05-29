''' 
Given an array A of N integers and also given two integers B and C. 
Reverse the elements of the array A within the given inclusive range [B, C].


contraints: 
1 <= N <= 105
1 <= A[i] <= 109
0 <= B <= C <= N - 1

'''

def reverse_in_range(A, B, C):
    """
    Reverse the elements of the array A within the given inclusive range [B, C].
    
    :param A: List of integers
    :param B: Start index of the range (inclusive)
    :param C: End index of the range (inclusive)
    :return: None (the array A is modified in place)
    """
    while B < C:
        A[B], A[C] = A[C], A[B]
        B += 1
        C -= 1
# Example usage:
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = 1
    C = 3
    reverse_in_range(A, B, C)
    print(A)  # Output: [1, 4, 3, 2, 5]




