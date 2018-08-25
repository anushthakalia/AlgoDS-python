def rotation(arr1, arr2):
    n=len(arr1)
    # left rotation
    arr1_left = arr1[2:]+ arr1[:2]
    arr1_right = arr1[-2:] + arr1[:n-2]
    print(arr1_left)
    print(arr1_right)
    if arr1_left == arr2:
        return 1
    elif arr1_right == arr2:
        return 1
    return 0
    

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		arr1 = input()
		arr2 = input()
		val = rotation(arr1, arr2)
		print(val)

# 	    wlrbbmqbhcdar
# owkkyhiddqscd
