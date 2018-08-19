
def bubble_sort(arr, n):
	for j in range(n-1):
		for i in range(1,n):
			if arr[i-1]>arr[i]:
				temp=arr[i]
				arr[i]=arr[i-1]
				arr[i-1]=temp
	return arr



if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		val = bubble_sort(arr,n)
		print(*val)