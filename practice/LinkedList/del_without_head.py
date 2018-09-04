# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node.next.val
        node.next.val = node.val
        node.val = temp
        
        node.next = node.next.next
        
        # so basically, here we copy the contents of adjacent nodes and then delete the next node
        # only applicable if node is not the tail