class Node:
	def __init__(self, data):
		self.data = data
		self.next_node = None

class SLinkedList():
	def __init__(self):
		self.head=None

	def printLL(self):
		printval = self.head
		while printval is not None:
			print(printval.data, end = ' ')
			printval = printval.next_node
		print()

sl = SLinkedList()
sl.head = Node('Hello')
e2 = Node('I am')
e3 = Node(1)
sl.head.next_node = e2
e2.next_node = e3

sl.printLL()