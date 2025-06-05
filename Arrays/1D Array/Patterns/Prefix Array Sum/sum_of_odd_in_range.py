'''
First Argument A, is a list of integers representing the array.
Second Argument B, is a 2D list where each sublist B[i]=[L,R] contains two integers L and R, representing the range for the query.

Return a list of integers where each integer is the result of the sum of elements at odd indices in the range [L, R] for each query.

A = [2, 8, 3, 9, 15]
B = [ [1, 4], 
      [0, 2], 
      [2, 3] ]

      

'''

def sum_of_odd_in_range(A):
    pfA = [0] * len(A);
    pfA[0] = 0;
    for i in range(1,len(A)):
        if(i%2!=0):
            pfA[i] = pfA[i-1]+A[i];
        else:
            pfA[i] = pfA[i-1];
    print(f"prefix subarray odd sum is :{pfA}");   
    return pfA;

def get_sum_odd_elements_in_range(A,B):
    queries = len(B);
    pfx = sum_of_odd_in_range(A);
    diff = [];
    for i in range(queries):
        l = B[i][0]
        r = B[i][1]
        if(l==0):
            suma = pfx[r];

        else:
            suma = pfx[r]-pfx[l-1];     
        diff.append(suma);
    print(f"prefix subarray  sum in {queries} : {B} given ranges is:{diff}");   
    return diff;

# Example usage:
if __name__ == "__main__":
    A = [2, 8, 3, 9, 15]
    B = [[1, 4],[0, 2],[2, 3],[0,4]];
    sum_of_odd_in_range(A);
    get_sum_odd_elements_in_range(A,B);
