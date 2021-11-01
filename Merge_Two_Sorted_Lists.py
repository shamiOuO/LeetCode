class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 =ListNode(1)

l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = []
l4 = ListNode(None)
pre = l4
while l1:
    l3.append(l1.val)
    l1 = l1.next
while l2:
    l3.append(l2.val)
    l2 = l2.next
for i in sorted(l3):
    pre.next = ListNode(i)
    pre = pre.next