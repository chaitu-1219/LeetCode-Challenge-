

class Solution:
    def singleNumber(self, nums):
        # Step 1: Initialize result to 0
        # 0 is the identity element for XOR (0 ^ x = x)
        res = 0
        
        # Step 2: Iterate through every number in the array
        for n in nums:
            # Step 3: XOR the current number with the running result
            # Key insight: a ^ a = 0 (a number XORed with itself cancels out)
            # and a ^ 0 = a (a number XORed with 0 stays unchanged)
            # So numbers appearing twice cancel out to 0,
            # leaving only the number that appears once as the final result
            res ^= n
        
        # Step 4: Return the single number
        return res


def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test cases:
    # Case 1: 2 appears once (4 appears twice, 1 appears twice)
    nums1 = [4, 1, 2, 1, 2]
    print(f"nums = {nums1} -> single number = {solution.singleNumber(nums1)}")  # Expected: 2
    
    # Case 2: 1 appears once (2 appears twice)
    nums2 = [2, 2, 1]
    print(f"nums = {nums2} -> single number = {solution.singleNumber(nums2)}")  # Expected: 1
    
    # Case 3: Single element array
    nums3 = [1]
    print(f"nums = {nums3} -> single number = {solution.singleNumber(nums3)}")  # Expected: 1


# Entry point: run main only when this script is executed directly
if __name__ == "__main__":
    main()
