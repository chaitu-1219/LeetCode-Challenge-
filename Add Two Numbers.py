class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Create a dummy node to simplify result list construction
        dummyHead = ListNode(0)

        # Tail pointer is used to add new nodes to the result list
        tail = dummyHead

        # Stores carry generated during addition
        carry = 0

        # Continue while there are nodes left in l1 or l2
        # or there is a remaining carry
        while l1 is not None or l2 is not None or carry != 0:

            # Get current digit from l1
            # If l1 is exhausted, use 0
            digit1 = l1.val if l1 is not None else 0

            # Get current digit from l2
            # If l2 is exhausted, use 0
            digit2 = l2.val if l2 is not None else 0

            # Add both digits and carry
            total = digit1 + digit2 + carry

            # Extract the digit to store in current node
            digit = total % 10

            # Calculate carry for next iteration
            carry = total // 10

            # Create a new node with the calculated digit
            newNode = ListNode(digit)

            # Attach new node to the result list
            tail.next = newNode

            # Move tail to the newly added node
            tail = tail.next

            # Move l1 to next node if available
            l1 = l1.next if l1 is not None else None

            # Move l2 to next node if available
            l2 = l2.next if l2 is not None else None

        # Skip dummy node and get actual result list
        result = dummyHead.next

        # Optional cleanup
        dummyHead.next = None

        # Return the head of the resulting linked list
        return result
