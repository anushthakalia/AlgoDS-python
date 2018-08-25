def parenthesis_checker(arr):
    left = '[({'
    right = '])}'
    temp = []
    print(type(arr))

    for i in arr:
        print('{} has temp {}'.format(i, temp))
        if i in left:
            temp.append(i)
        elif i in right:
            if len(temp)==0:
                print('not balanced')
            else:
                temp.pop()


    print(temp)
    if len(temp)==0:
        print('balanced')
    else:
        print('not balanced')

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		
		arr = input()
		parenthesis_checker(arr)
		#print(result)