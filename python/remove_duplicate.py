'''''''''''''''''''''''''''''''''''''''''''''''''''
  > System:		Ubuntu
  > Author:		ty-l6
  > Mail:		liuty196888@gmail.com
  > File Name:		remove_duplicate.py
  > Created Time:	2017-08-18 Fri 00:21
'''''''''''''''''''''''''''''''''''''''''''''''''''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicate(head):
    '''
    :type head: ListNode
    :rtype: ListNode
    '''
    if not head or not head.next: return head
    current = head.next
    prev = head
    while current:
        if prev.val == current.val:
            prev.next = current.next
            current = prev.next
        else:
            prev = prev.next
            current = current.next
    return head
