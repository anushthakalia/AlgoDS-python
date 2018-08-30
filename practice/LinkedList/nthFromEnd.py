def getNthFromLast(head, n):
    temp = head
    count=1
    while temp.next!=None:
        count+=1
        temp = temp.next
    
    if n>count:
        return -1
    else:
        k=count-n+1
        temp = head
        ctr=1
        while(ctr<k):
            temp=temp.next
            ctr+=1
        return temp.data
    # Code here


# try out using two pointers - reference and main pointer (though same time complexity of O(n))