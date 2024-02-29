#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find nkth smallest element and return using this function
        '''
        temp_arr = arr
        min_pointer = 0
        for i in range(k):
            for i in range(0,r-1):
                if temp_arr[i]<temp_arr[i+1]:
                    min_pointer = i
                temp_arr.remove(arr[i])
        return min_pointer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends
