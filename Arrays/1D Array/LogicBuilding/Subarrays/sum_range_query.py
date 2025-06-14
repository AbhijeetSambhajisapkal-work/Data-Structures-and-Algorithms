'''

You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.



constraints
1 <= N, M <= 105
1 <= A[i] <= 109
0 <= L <= R < N


Output Format
Return an integer array of length M where ith element is the answer for ith query in B.


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]

'''


def sum_range_query(A,B):
    queries = len(B);

    PFA = [0] * len(A);
    PFA[0] = A[0];
    for I in range(len(A)):
        PFA[I] = PFA[I-1] + A[I];

    SumA =[0] * queries;
    for i in range(queries):
        l = B[i][0];
        r = B[i][1];
        if(l==0):
            SumA[i] = PFA[r];
        else:
            SumA[i] = PFA[r] - PFA[l-1];
    
    print(SumA);
                

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = [[0, 3], [1, 2]]
    sum_range_query(A,B) # 1,[1,2], [1,2,3],[1,2,3,4]......

