def print_all_subarrys(array):
    for i in range(len(array)):
       for j in range(i,len(array)): 
           for k in range(i,j):
               print(array[k]);

def print_all_subarrys_sum(array):
    sum_of_subarray_array = [];
    for i in range(len(array)):
       for j in range(i,len(array)): 
            sum_of_subarray = 0;
            sum_of_subarray = sum_of_subarray + array[k];
            sum_of_subarray_array.append(sum_of_subarray);
    print(sum_of_subarray_array);

'''

        prefixsumarray = [];
        prefixsumarray[0] = nums[0];
        for i in range(1,len(nums)):
            prefixsumarray[i] = prefixsumarray[i-1] + nums[i];



'''

# Example usage:
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    print_all_subarrys_sum(A) # 1,[1,2], [1,2,3],[1,2,3,4]......