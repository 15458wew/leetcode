class listnode():
    def __init__(self,x):
        self.val=x
        self.next=None

class solution():
    def mergetwolists(self,l1,l2):
        dummy=listnode(0)
        cur=dummy

        if not l1 and not l2:
            return None

        while l1 and l2:
            if l1.val>l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2.val
                l2=l2.next
            cur=cur.next
        cur.next=l1 or l2
        return dummy.next
