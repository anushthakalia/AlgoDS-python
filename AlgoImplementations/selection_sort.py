


def selection_sort(arr, n):

	for i in range(n-1):
		imin = i
		for j in range(i+1,n):
			if arr[j]<arr[imin]:
				imin = j
		temp = arr[i]
		arr[i]=arr[imin]
		arr[imin]=temp

	return arr



if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		val = selection_sort(arr,n)
		print(*val)