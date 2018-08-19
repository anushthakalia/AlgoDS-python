# Naive solution consisting of two loops; time complexity O(n2)
# this solutions reads the array from right, time complexity O(n)

def leader(arr, n):
    max = arr[-1]
    leaders=[]
    leaders.append(max)
    for i in range(1,n+1):
        if arr[-i]>max:
            max=arr[-i]
            leaders.append(arr[-i])
    return leaders
        
    
if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		val = leader(arr,n)
		print(*val[::-1])