# insertion sort; best case O(n); worst case O(n^2);  space O(1)

def insertion_sort(arr, n):
	for i in range(1,n):
		key = arr[i]
		j=i-1
		while (j>=0) and (arr[j]>key):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key
	return arr



if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		val = insertion_sort(arr,n)
		print(*val)