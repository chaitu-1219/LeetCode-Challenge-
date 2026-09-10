class Solution:
    def majorityElement(self, nums):
        # Boyer-Moore Voting Algorithm
        # Key idea: since the majority element appears more than n/2 times,
        # it can "cancel out" every other element and still survive.

        # Start with the first element as our initial guess for the candidate
        candidate, count = nums[0], 0

        for num in nums:
            if num == candidate:
                # Same as current candidate -> strengthen its "vote"
                count += 1
            elif count == 0:
                # All previous support was cancelled out;
                # adopt this new number as the candidate
                candidate, count = num, 1
            else:
                # Different number -> cancel one vote for the candidate
                count -= 1

        # Because a majority element always exists, whichever candidate
        # survives the cancellation phase must be that majority element.
        return candidate


# Main method to test the solution
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [3, 2, 3],               # -> 3
        [2, 2, 1, 1, 1, 2, 2],   # -> 2
        [1],                     # -> 1
        [1, 1, 1, 2, 2, 2, 1],   # -> 1
        [5, 5, 5, 5],            # -> 5
    ]

    for nums in test_cases:
        result = sol.majorityElement(nums)
        print(f"Input: {nums}  ->  Majority Element: {result}")
