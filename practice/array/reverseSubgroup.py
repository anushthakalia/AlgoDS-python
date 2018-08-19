def reverseSubgrp(arr, n, k):
#     for i in range(0,n,k): print(*list(reversed(arr[i:i+k])), end=' ')
    a = []
    for i in range(0,n,k): 
        a.extend(arr[-(n-k-i)-1:-(n-i)-1:-1])
    a.extend(arr[n-n%k:][::-1])
    return a 
if __name__ == '__main__':
	n = int(input())
	for _ in range(n):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		k = int(input())
		a = reverseSubgrp(arr, n, k)
		print(*a)

# time complexity: O(n*k), space = O(n)
# can be done with space = O(1), by simply using print statement inside the function