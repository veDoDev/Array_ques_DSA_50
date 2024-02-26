#User function Template for python3

def getMinMax( a, n):
    min_pointer = 0
    max_pointer = 0
    pointer = 0
    for i in range(n):
        if a[pointer]<a[min_pointer]:
            min_pointer = pointer
        if a[pointer]>a[max_pointer]:
            max_pointer = pointer
        pointer += 1
    return a[min_pointer],a[max_pointer]
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
