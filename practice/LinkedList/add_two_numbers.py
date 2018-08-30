# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = l1
        num1,k=0,1
        while temp!=None:
            num1+=temp.val*k
            temp = temp.next
            k=k*10
        
        temp = l2
        num2, k = 0,1
        while temp!=None:
            num2+=temp.val*k
            temp = temp.next
            k=k*10
        final = str(num1+num2)
        head=ListNode(final[-1])
        temp1= head
        for i in range(len(final)-2,-1,-1):
            temp1.next = ListNode(final[i])
            temp1=temp1.next
        temp1.next=None
        return head
            