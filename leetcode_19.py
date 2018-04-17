class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None

class solution():
    def removeNthpoint(self,n,head):
          dummy=ListNode(0)
          dummy.next=head
          p,q=dummy,dummy

          for i in range(n):
              p=p.next

          while p.next:
              p=p.next
              q=q.next
          rec=q.next
          q.next=rec.next

          return dummy.next

