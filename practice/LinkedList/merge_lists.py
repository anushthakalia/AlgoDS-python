def mergeLists(head1, head2):
    if (head1 == None) and (head2==None):
        return None
    elif head1 == None:
        return head2
    elif head2 == None:
        return head1
    else:
        if head1.data < head2.data:
            pri = head1
            orp = pri
            sec = head2
        else:
            pri = head2
            orp = pri
            sec = head1
            
        while (pri.next!=None):
            if sec==None:
                return orp
            if pri.next.data > sec.data:
                temp = pri.next
                pri.next = sec
                sec = sec.next
                pri.next.next = temp
                pri = pri.next
            else:
                pri = pri.next
        if sec!=None:
            pri.next=sec
        return orp
                