from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point of the merged list.
        # This avoids needing special handling for the head of the result.
        dummy = ListNode()
        # 'cur' tracks the last node of the merged list as we build it.
        cur = dummy

        # Keep merging while both lists still have nodes remaining.
        while list1 and list2:
            # If list2's current node is smaller, attach it to the result.
            if list1.val > list2.val:
                cur.next = list2          # link the smaller node (from list2)
                list2 = list2.next        # advance list2 pointer
            # Otherwise, list1's node is smaller or equal, attach it.
            else:
                cur.next = list1          # link the smaller node (from list1)
                list1 = list1.next        # advance list1 pointer

            cur = cur.next                # move 'cur' forward to the new tail

        # One of the two lists is now exhausted.
        # Append whatever remains of the other list (it's already sorted).
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        # 'dummy.next' is the actual head of the merged list.
        return dummy.next


# Helper to build a linked list from a Python list (for testing).
def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# Helper to convert a linked list back to a Python list (for printing).
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def main():
    sol = Solution()

    # Test case 1: both lists have elements
    list1 = build_list([1, 2, 4])
    list2 = build_list([1, 3, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print("Test 1:", to_list(merged))          # Expected: [1, 1, 2, 3, 4, 4]

    # Test case 2: one list is empty
    list1 = build_list([])
    list2 = build_list([0])
    merged = sol.mergeTwoLists(list1, list2)
    print("Test 2:", to_list(merged))          # Expected: [0]

    # Test case 3: both lists empty
    list1 = build_list([])
    list2 = build_list([])
    merged = sol.mergeTwoLists(list1, list2)
    print("Test 3:", to_list(merged))          # Expected: []

    # Test case 4: one list is much longer
    list1 = build_list([1, 3, 5, 7, 9])
    list2 = build_list([2, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print("Test 4:", to_list(merged))          # Expected: [1, 2, 3, 4, 5, 7, 9]


if __name__ == "__main__":
    main()
