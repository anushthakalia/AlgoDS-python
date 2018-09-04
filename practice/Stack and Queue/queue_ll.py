
class Node():
	def __init__(self,data):
		self.data = data
		self.next = None

class Queue():
	def __init__(self):
		self.head = None # if I maintain a tail pointer, then won't need to traverse the whole queue

	def enqueue(self, data):
		print('enqueuing',end=' ')
		temp = self.head
		self.head = Node(data)
		self.head.next = temp

	def dequeue(self):
		print('dequeing',end=' ')
		if self.head==None:
			print('Queue empty!')
		else:
			temp = self.head
			while temp.next.next != None:
				temp = temp.next

			temp.next = None

	def peek(self):
		temp = self.head

		while temp.next!=None:
			temp = temp.next

		print('Peeking the front: {}'.format(temp.data))

	def is_empty(self):
		if self.head==None:
			return True
		else:
			return False

	def print_queue(self):
		temp = self.head
		while temp!=None:
			print(temp.data, end = ' ')
			temp = temp.next
		print()

if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = list(map(int, input().rstrip().split()))
		k = 0
		q = Queue()
		while k<len(arr):
			if arr[k]==1:
				q.enqueue(arr[k+1])
				k+=2
			else:
				q.dequeue()
				k+=1
			q.print_queue()
		q.peek()



