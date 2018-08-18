def subseqSum(A, n):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

    
    
if __name__ == '__main__':
	n = int(input())
	for _ in range(n):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		val = subseqSum(arr, n)
		print(val)