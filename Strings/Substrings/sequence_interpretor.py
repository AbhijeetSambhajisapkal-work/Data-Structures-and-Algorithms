'''
You have given a string A having Uppercase English letters.
You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.

Problem Constraints
1 <= length(A) <= 105

Input Format
First and only argument is a string A.


Output Format
Return an long integer denoting the answer.


Example Input
Input 1:
A = "ABCGAG"

counter for A hold counter for A while looping checking for G once G found increase countofG



Example Output
Output 1:
 3


'''


def sequence_interpretor(A):
        counta=0;
        countag=0;
        for i in range(len(A)):
            if(A[i] == 'A'):
                counta = counta+1;
            elif(A[i] == 'G'):
                countag=countag+counta;
        return countag

# Example usage: 
if __name__ == "__main__":
    A = 'AGAGAGA';
    temp = sequence_interpretor(A);
    print(temp); 

