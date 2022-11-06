import merge_two_sorted

def testcases(exp: str, s:merge_two_sorted.Solution,  l1: merge_two_sorted.ListNode, l2: merge_two_sorted.ListNode):
    print("--------------- Teste iniciado ---------------")
    print("expected = " + exp + "\noutput   =", end=" ")

    obj = s.mergeTwoLists(l1, l2)

    while(obj != None):
        print(obj.val, end=" ")
        obj = obj.next
    print("")
    print("--------------- Teste finalizado ---------------")

s = merge_two_sorted.Solution()

a2 = merge_two_sorted.ListNode(4, None)
a1 = merge_two_sorted.ListNode(2, a2)
a  = merge_two_sorted.ListNode(1, a1)

b2 = merge_two_sorted.ListNode(4, None)
b1 = merge_two_sorted.ListNode(3, b2)
b  = merge_two_sorted.ListNode(1, b1)

testcases("1 1 2 3 4 4", s, a, b)

testcases("", s, None, None)

a = merge_two_sorted.ListNode(0, None)

testcases("0", s, a, None)

