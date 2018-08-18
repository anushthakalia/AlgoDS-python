def missing(arr):
    arr.sort()
    if (len(arr)==1) and arr[0]==1:
        return arr[0]+1
    elif (len(arr)==1) and arr[0]==2:
        return arr[0]-1
    else:   
    	for i in range(len(arr)):
    		if (i+1<len(arr)) and (arr[i+1]-arr[i]==2):
    			return arr[i]+1
    if arr[0]!=1:
        return 1
    else:
        return arr[-1]+1


if __name__ == '__main__':
	n = int(input())
	for _ in range(n):
		l = int(input())
		arr = list(map(int, input().rstrip().split()))
		val = missing(arr)
		print(val)