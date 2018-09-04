
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack():
	def __init__(self):
		self.head = None

	def push(self, data):
		print('Pushing {} to the stack'.format(data))
		temp = self.head
		self.head = Node(data)
		self.head.next = temp

	def pop(self):
		if self.head == None:
			print('Cannot pop. LinkedList already empty.')
		else:
			print('Popping {} from the stack '.format(self.head.data))
			self.head = self.head.next

	def peek(self):
		print(self.head.data)

	def is_empty(self):
		if self.head==None:
			return True
		else:
			return False

	def print_stack(self):
		print('Stack now is:', end=' ')
		temp = self.head
		while temp != None:
			print(temp.data, end = ' ')
			temp = temp.next
		print()



if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		k = 0
		s = Stack()
		while k<len(arr):
			if arr[k]==1:
				s.push(arr[k+1])
				k+=2
			else:
				s.pop()
				k+=1
			s.print_stack()





