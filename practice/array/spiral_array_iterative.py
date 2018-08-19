# spiral matrix



def spiral_iter(arr):
	# if len(arr)==1:
	# 	print(arr[0])
	# 	return arr[0]
	m = len(arr)
	n = len(arr[0])
	i,j=0,0
	l=[]

	while(i<=(m-1-i) or j<=(n-1-j)):
		if i==m-1-i:
			l.extend(arr[i][j:n-j])
			# print(arr[i][j:n-j])
			i+=1
			j+=1
			continue


		l.extend(arr[i][j:n-j])
		l.extend([row[n-1-j] for row in arr[i:m-i]][1:])
		l.extend(arr[m-1-i][j:n-j][::-1][1:])
		l.extend([row[j] for row in arr[i:m-i]][::-1][1:-1])
		# print(arr[i][j:n-j])
		# print([row[n-1-j] for row in arr[i:m-i]][1:])
		# print(arr[m-1-i][j:n-j][::-1][1:])
		# print([row[j] for row in arr[i:m-i]][::-1][1:-1])
		i+=1
		j+=1
	return l




if __name__ == '__main__':
	arr = [[1,2],[3,4],[5,6]]
	print(arr)
	print('Now printing the spiral order')
	li=spiral_iter(arr)
	print(li)


