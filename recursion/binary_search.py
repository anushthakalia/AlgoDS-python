# binary search - recursion

def search(arr, target, low , high):
	med = (low + high)/2
	if low>high:
		print "Binary search unsuccesful"
		return

	elif arr[med] == target:
		print 'Target identified at index {}'.format(med)
		return

	elif arr[med] < target:
		search(arr, target, med+1, high)

	elif arr[med] > target:
		search(arr, target, low, med-1)
	return



def main():
	
	arr = [2,4,5,6,8,9,10]
	low = 0
	high = len(arr)-1
	target = 11
	search(arr, target, low, high)

main()
