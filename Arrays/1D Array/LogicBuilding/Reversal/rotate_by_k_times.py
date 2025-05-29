def rotate_by_k_times(A,k):
    k = k % len(A); # handle case when k > n
    reverse(A,0,len(A)-1);
    reverse(A,0,k-1);
    reverse(A,k,len(A)-1);
    return A;


def reverse(A,s,e):
    while(s<e):
        temp=A[s];
        A[s]=A[e];
        A[e]=temp;
        s=s+1;
        e=e-1;
    return A;


# Example usage:
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    k = 3
    rotate_by_k_times(A,k)
    print(A)  # Output: [1, 4, 3, 2, 5]