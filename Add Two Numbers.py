# Definition for singly-linked list.
class ListNode:
    """Represents a single node in a linked list."""
    def __init__(self, val=0, next=None):
        self.val = val    # The value stored in this node
        self.next = next  # Reference to the next node (None if last)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds two numbers represented as reversed linked lists.
        Each node contains a single digit, stored in reverse order,
        so the head is the least significant digit.

        e.g., 342 -> 2 -> 4 -> 3
              465 -> 5 -> 6 -> 4
              Sum  = 807 -> 7 -> 0 -> 8

        Args:
            l1: First number as a reversed linked list
            l2: Second number as a reversed linked list

        Returns:
            The sum as a reversed linked list
        """
        # Dummy head avoids special-casing the first node
        dummyHead = ListNode(0)
        tail = dummyHead  # Points to the last node built so far
        carry = 0         # The digit carried over from the previous column

        # Continue until both lists are exhausted AND there is no leftover carry
        while l1 is not None or l2 is not None or carry != 0:
            # Get the current digit from each list (0 if the list is exhausted)
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            # Sum the two digits plus any carry
            sum = digit1 + digit2 + carry

            # The current result digit is the units place of the sum
            digit = sum % 10
            # The carry for the next column is the tens place
            carry = sum // 10

            # Append the new digit to the result list
            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            # Advance both lists (they become None once fully consumed)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # 'result' points to the real first node (skip the dummy head)
        result = dummyHead.next
        dummyHead.next = None  # Optional: detach dummy head for cleanup
        return result


def list_to_linked_list(nums):
    """Helper: convert a Python list of digits into a reversed linked list."""
    dummy = ListNode(0)
    tail = dummy
    for num in nums:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next


def linked_list_to_list(head):
    """Helper: convert a reversed linked list back into a Python list (for printing)."""
    nums = []
    while head is not None:
        nums.append(head.val)
        head = head.next
    return nums


def main():
    """Test the addTwoNumbers solution with sample cases."""
    solution = Solution()

    # Test case 1: 342 + 465 = 807
    # 342 -> reversed: [2, 4, 3]
    # 465 -> reversed: [5, 6, 4]
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 1: [2,4,3] + [5,6,4] =", linked_list_to_list(result))
    print("Expected: [7,0,8]\n")

    # Test case 2: 0 + 0 = 0
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 2: [0] + [0] =", linked_list_to_list(result))
    print("Expected: [0]\n")

    # Test case 3: Unequal lengths + carry overflow
    # 9999999 + 9999 = 10009998
    # 9,999,999 -> [9,9,9,9,9,9,9]
    # 9,999     -> [9,9,9,9]
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 3: [9,9,9,9,9,9,9] + [9,9,9,9] =", linked_list_to_result(result))
    print("Expected: [8,9,9,9,0,0,0,1]\n")

    # Test case 4: Carry creates an extra digit
    # 5 + 5 = 10
    l1 = list_to_linked_list([5])
    l2 = list_to_linked_list([5])
    result = solution.addTwoNumbers(l1, l2)
    print("Test 4: [5] + [5] =", linked_list_to_result(result))
    print("Expected: [0,1]")


if __name__ == "__main__":
    main()
