# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = []
        arr2 = []
        qty1 = int(1)
        qty2 = int(1)
        a = l1
        b = l2
        while(a.next != None): #transform liked list to array
            arr1.insert(qty1 - 1 , a.val)
            qty1 += 1
            a = a.next
        arr1.insert(qty1 - 1 , a.val)

        num1 = 0

        for x in range(0, qty1): #transform array to int
            num1 = num1 + arr1[x]*pow(10, x)

        while(b.next != None): #transform liked list to array
            arr2.insert(qty2 - 1 , b.val)
            qty2 += 1
            b = b.next
        arr2.insert(qty2 - 1 , b.val)

        num2 = 0
        for x in range(0, qty2): #transform array to int
            num2 = num2 + arr2[x]*pow(10, x)

        num = num1 + num2

        arr = []
        qty = 1

        while(num > 0): #retransform to array
            arr.insert(qty - 1, num % 10)
            num = int(num/10)

        #Retransform to a linked list
        
        print(arr)


a = ListNode(3, None)
b = ListNode(4, a)
c = ListNode(2, b) #start of linked list

d = ListNode(4, None)
e = ListNode(6, d)
f = ListNode(5, e) #start of linked list

s = Solution()

print("expected =  \noutput   = " + str(s.addTwoNumbers(c, f)))


