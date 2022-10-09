Optional=0
ListNode=" "
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False;
        slow = head;
        fast = head;
        while fast.next != None and fast.next.next != None:
            slow = slow.next;
            fast = fast.next.next;
            if slow == fast:
                return True;
        return False
