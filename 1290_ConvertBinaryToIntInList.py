"""
        :type head: ListNode
        :rtype: int
"""
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getDecimalValue(head):
    prev = None
    while (head):
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    value = 0
    count = 0

    while (prev):
        if prev.val == 1:
            value += 2**count
        count += 1
        prev = prev.next
    return value

print(getDecimalValue([1,0,1]))
