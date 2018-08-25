def reverse_sentance(arr):
    print('.'.join(arr.split('.')[::-1]))
if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		arr = input()
		reverse_sentance(arr)