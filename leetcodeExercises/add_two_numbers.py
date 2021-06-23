"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    placeholder = cur = ListNode(0)     #Placeholder for the linkedlist of added values.
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next 
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10) #Get value for the current digit.
        cur = cur.next
        carry //= 10                    #Remainder is carried over to next digit.

    return placeholder.next                   

#LinkedList initializing
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

def printList(ln):
    while ln != None:
        print(ln.val)
        ln = ln.next

summedList = addTwoNumbers(l1, l2)
printList(summedList)