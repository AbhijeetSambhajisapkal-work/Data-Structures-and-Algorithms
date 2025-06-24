'''
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
and at least one occurrence of the minimum value of the array.

Problem Constraints
1 <= |A| <= 2000


Input Format
First and only argument is vector A


Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array




Example Input
Input 1:
A = [1, 3, 2]
Input 2:
A = [2, 6, 1, 6, 9]


Example Output
Output 1:
 2
Output 2:
 3
'''


# sort it
# then check from end to first element if element is minmum return subarray  
# 1 2 3 array its self is the answer 


def min_max_subrray(A):
    length =  len(A);
    A.sort();
    minnum = min(A);
    windowendindex = 0;
    for i in range(len(A)-1,-1,-1):
        if(A[i]==minnum):
            windowendindex = i;

    print(len(A)-windowendindex);


if __name__ == "__main__":
    A = [2, 6, 1, 6, 9]
    min_max_subrray(A) # 1,[1,2], [1,2,3],[1,2,3,4]......

