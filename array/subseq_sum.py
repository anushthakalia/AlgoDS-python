# subsequence sum

def subseq(arr,n, s):
    for i in range(n):
        for j in range(i+1, n+1):
            if sum(arr[i:j])==s:
                return [i+1,j]
                
    return [-1]

if __name__ == '__main__':
	n = int(input())
	for _ in range(n):
		n, s = list(map(int, input().rstrip().split()))
		arr = list(map(int, input().rstrip().split()))
		val = subseq(arr,n, s)
		print(*val)