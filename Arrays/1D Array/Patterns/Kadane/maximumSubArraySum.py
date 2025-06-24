def maxSubArray(self, A):
        sumo = 0;
        ans = -1000000000000000000000000;
        for i in range(len(A)):
            sumo = sumo + A[i];
            ans = max(ans,sumo);
            if(sumo < 0):
                sumo = 0;     
        print(ans);

if __name__ == "__main__":
    A = [-2, -8, 3, 9, -15]
    maxSubArray(A);