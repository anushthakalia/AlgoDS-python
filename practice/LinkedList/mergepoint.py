def findMergeNode(head1, head2):
    temp = head1 
    s = set([])
    while temp.next!=None:
        s.add(temp)
        temp=temp.next
    s.add(temp)
    
    prev = head2
    while prev.next!=None:
        if prev in s:
            return prev.data
        prev = prev.next
    return -1