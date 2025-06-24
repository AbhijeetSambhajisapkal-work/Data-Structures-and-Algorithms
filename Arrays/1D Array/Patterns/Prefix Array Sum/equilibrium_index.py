def equilibirum_index(A):
    length = len(A);
    PFA = [0]* length;
    PFA[0] = A[0];
    for i in range(1,length):
        PFA[i] = PFA[i-1] + A[i];

    for i in range(length):
        leftsum = PFA[i] - A[i];
        rightsum = PFA[length-1] - PFA[i];
        if(leftsum == rightsum):
            return i;
    
    return -1;

if __name__ == "__main__":
    A = [-7,1,5,2,-4,3,0];
    X = [2,-2,2]
    temp = equilibirum_index(X);
    print(temp); 