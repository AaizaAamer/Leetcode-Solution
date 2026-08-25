class Solution(object):
    def addTwoNumbers(self, l1, l2):
        cur1 = l1
        cur2 = l2
        carry = 0
        output = ListNode(0)
        current = output

        while cur1 or cur2 or carry:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        return output.next
