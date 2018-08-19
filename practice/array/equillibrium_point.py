# def equi(arr, n): # O(n*k) solution
#     if n==1:
#         return 1
    
#     for i in range(n):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i+1
    
#     return -1

# O(n) solution
def equi(arr, n):
    if n==1:
        return 1
    s = sum(arr)
    left_sum=0
    for i in range(n):
        if left_sum == s-arr[i]-left_sum:
            return i+1
        else:
            left_sum += arr[i]
    
    return -1
    
if __name__ == '__main__':
	n = int(input())
	for _ in range(n):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		val = equi(arr,n)
		print(val)