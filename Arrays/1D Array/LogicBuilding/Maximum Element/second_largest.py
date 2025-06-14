def second_largest(A):
    largest_number = A[0];
    largest_index = 0;
    for x in range(1,len(A)):
        if(A[x] > largest_number):
            largest_number = A[x];
            largest_index = x;

    second_largest = A[0];
    for x in range(0,len(A)):
        if(x != largest_index and A[x] != largest_number):
            if(A[x] > second_largest):
                second_largest= A[x];

    print(second_largest);
    
if __name__ == "__main__":
    A = [1, 4, 4, 5, 5]
    second_largest(A) # 1,[1,2], [1,2,3],[1,2,3,4]...... 