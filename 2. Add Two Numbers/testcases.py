import add_two_numbers

def testcases(exp: str, s:add_two_numbers.Solution,  l1: add_two_numbers.ListNode, l2: add_two_numbers.ListNode):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + exp + "\noutput   =", end=" ")

    obj = s.addTwoNumbers(l1, l2)

    while(obj != None):
        print(obj.val, end=" ")
        obj = obj.next
    print("")
    print("--------------- Teste finalizado ---------------")

s = add_two_numbers.Solution()

a2 = add_two_numbers.ListNode(3, None)
a1 = add_two_numbers.ListNode(4, a2)
a =  add_two_numbers.ListNode(2, a1) #start of linked list

b2 = add_two_numbers.ListNode(4, None)
b1 = add_two_numbers.ListNode(6, b2)
b =  add_two_numbers.ListNode(5, b1) #start of linked list

testcases("7 0 8", s, a, b)

b = add_two_numbers.ListNode(0, None) #start of linked list

a = add_two_numbers.ListNode(0, None) #start of linked list

testcases("0", s, a, b)

a7 = add_two_numbers.ListNode(9, None)
a6 = add_two_numbers.ListNode(9, a7)
a5 = add_two_numbers.ListNode(9, a6)
a4 = add_two_numbers.ListNode(9, a5)
a3 = add_two_numbers.ListNode(9, a4)
a2 = add_two_numbers.ListNode(9, a3)
a  = add_two_numbers.ListNode(9, a2) #start of linked list

b3 = add_two_numbers.ListNode(9, None)
b2 = add_two_numbers.ListNode(9, b3)
b1 = add_two_numbers.ListNode(9, b2)
b  = add_two_numbers.ListNode(9, b1) #start of linked list

testcases("8 9 9 9 0 0 0 1", s, a, b)

a7 = add_two_numbers.ListNode(9, None)
a6 = add_two_numbers.ListNode(9, a7)
a5 = add_two_numbers.ListNode(9, a6)
a4 = add_two_numbers.ListNode(9, a5)
a3 = add_two_numbers.ListNode(9, a4)
a2 = add_two_numbers.ListNode(9, a3)
a  = add_two_numbers.ListNode(9, a2) #start of linked list

b3 = add_two_numbers.ListNode(9, None)
b2 = add_two_numbers.ListNode(9, b3)
b1 = add_two_numbers.ListNode(9, b2)
b  = add_two_numbers.ListNode(9, b1) #start of linked list

#for i in range(0, 19):
#    print(int(i/10))