# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Use two pointers: 'fast' and 'slow', both starting at the head.
        # The idea is to advance 'fast' by n steps first, then move both
        # pointers together. When 'fast' reaches the end, 'slow' will be
        # pointing at the node just before the one we need to remove.
        fast, slow = head, head
        
        # Advance 'fast' n steps ahead of 'slow'.
        for _ in range(n):
            fast = fast.next
        
        # If 'fast' is None, it means we need to remove the head node
        # (i.e., n equals the length of the list). Handle this edge case.
        if not fast:
            return head.next
        
        # Move both pointers together until 'fast' reaches the last node.
        # At this point 'slow' points to the node right before the nth node
        # from the end.
        while fast.next:
            fast, slow = fast.next, slow.next
        
        # Skip the target node by linking 'slow' to the node after it.
        slow.next = slow.next.next
        
        # Return the (possibly unchanged) head of the list.
        return head

def main():
    # Helper function to build a linked list from a list of integers.
    def build_list(vals):
        dummy = ListNode(0)
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    # Helper function to convert a linked list into a Python list for printing.
    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    solution = Solution()

    # Test case 1: remove the 2nd node from the end of [1,2,3,4,5]
    head = build_list([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 2)
    print("Input:  [1,2,3,4,5], n=2")
    print("Output:", to_list(result))  # Expect [1,2,3,5]

    # Test case 2: single node, remove 1st from end -> empty list
    head = build_list([1])
    result = solution.removeNthFromEnd(head, 1)
    print("Input:  [1], n=1")
    print("Output:", to_list(result))  # Expect []

    # Test case 3: remove the head node
    head = build_list([1, 2])
    result = solution.removeNthFromEnd(head, 2)
    print("Input:  [1,2], n=2")
    print("Output:", to_list(result))  # Expect [2]

if __name__ == "__main__":
    main()
