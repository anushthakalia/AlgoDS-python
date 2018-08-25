
def merge(arr, p, q, r):
	n1 = q-p+1
	n2=r-q

	L=[0]*(n1+1)
	R=[0]*(n2+1)

	for i in range(0,n1):
		L[i]=arr[p+i]

	for i in range(0,n2):
		R[i]=arr[q+1+i]


	L[-1]=100000
	R[-1]=100000

	i,j=0,0

	for k in range(p,r+1):
		if L[i]<R[j]:
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1



def mergesort(arr, p, r):
	if p<r:
		q=(p+r)//2
		mergesort(arr, p, q)
		mergesort(arr, q+1, r)
		merge(arr, p, q, r)
	print(arr)



if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		mergesort(arr,0,n-1)