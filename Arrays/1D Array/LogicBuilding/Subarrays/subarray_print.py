def print_all_subarrys(array):
    for i in range(len(array)):
       for j in range(i,len(array)): 
           for k in range(i,j):
               print(array[k]);

# Example usage: 
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    print_all_subarrys(A) # 1,[1,2], [1,2,3],[1,2,3,4]......

