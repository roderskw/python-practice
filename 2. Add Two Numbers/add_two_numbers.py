# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        linkedlist = []
        val = 0

        while(l1 != None or l2 != None or val == 1):
            #all possible cases of sum value for l1 and l2
            if(l1 == None and l2 == None): val = 1
            elif(l1 == None)             : val = val + l2.val
            elif(l2 == None)             : val = val + l1.val
            else                         : val = val + l1.val + l2.val

            #append new node(val 0-9) to linked list, update val value to a possible carry
            linkedlist.append(ListNode(val%10, None))
            val = int(val/10)

            #update previous node with new node created if a previous node exists
            if(len(linkedlist) > 1):
                linkedlist[len(linkedlist) - 2].next = linkedlist[len(linkedlist) - 1]

            #update nodes to next node
            if(l1 != None): l1 = l1.next 
            if(l2 != None): l2 = l2.next 

        return linkedlist[0]