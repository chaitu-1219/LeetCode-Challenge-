class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node to start the result list
        dummy = ListNode()

        # Store the head of the result list
        res = dummy

        # Initialize total and carry
        total = carry = 0

        # Continue while there are nodes left in l1, l2, or a carry exists
        while l1 or l2 or carry:

            # Start with the carry from the previous iteration
            total = carry

            # Add current value from l1 if available
            if l1:
                total += l1.val
                l1 = l1.next

            # Add current value from l2 if available
            if l2:
                total += l2.val
                l2 = l2.next

            # Get the digit to store in the new node
            num = total % 10

            # Calculate carry for the next iteration
            carry = total // 10

            # Create a new node and attach it to the result list
            dummy.next = ListNode(num)

            # Move dummy pointer to the newly created node
            dummy = dummy.next

        # Return the actual head of the result list
        return res.next
