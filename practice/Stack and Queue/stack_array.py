
class Stack():
	def __init__(self, maxsize=10):
		self.stack = []
		self.maxsize = maxsize
		self.top = 0

	def push(self,data):
		if self.top==self.maxsize:
			print("Stack Full! Cannot push more objects")

		else:
			print('Pushing element: {}'.format(data))
			self.stack.append(data)
			self.top+=1

	def pop(self):
		if self.top==0:
			print('Stack empty! Cannot pop.')

		else:
			print('Popping element : {}'.format(self.stack[self.top-1]))
			self.stack.pop()
			self.top-=1

	def peek(self):
		print(self.stack[self.top-1])

	def is_empty(self):
		if self.top==0:
			return True
		else:
			return False

	def print_stack(self):
		for i in range(self.top):
			print(self.stack[i], end = ' ')
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
