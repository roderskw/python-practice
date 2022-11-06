# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        linkedlist = [] 
        if(list1 == None and list2 == None):
            return None
        while(list1 != None or list2 != None):

            if(list2 == None and list1 != None):
                linkedlist.append(ListNode(list1.val, None))
                list1 = list1.next

            elif(list1 == None and list2 != None):
                linkedlist.append(ListNode(list2.val, None))
                list2 = list2.next

            elif(list1.val <= list2.val):
                linkedlist.append(ListNode(list1.val, None))
                list1 = list1.next

            else:
                linkedlist.append(ListNode(list2.val, None))
                list2 = list2.next
            
            if(len(linkedlist) > 1):
                linkedlist[len(linkedlist) - 2].next = linkedlist[len(linkedlist) - 1]

        return linkedlist[0]