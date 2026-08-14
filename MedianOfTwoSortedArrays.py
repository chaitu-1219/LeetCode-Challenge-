class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Combine both arrays into one array
        merged = nums1 + nums2

        # Sort the combined array
        merged.sort()

        # Find the total number of elements
        total = len(merged)

        # Check whether the total number of elements is odd
        if total % 2 == 1:

            # For odd length, the middle element is the median
            middle = total // 2

            return float(merged[middle])

        else:

            # For even length, there are two middle elements

            # Index of first middle element
            middle1 = total // 2 - 1

            # Index of second middle element
            middle2 = total // 2

            # Calculate the average of the two middle elements
            median = (merged[middle1] + merged[middle2]) / 2

            return float(median)


# Main method
if __name__ == "__main__":

    # Read first array
    nums1 = list(map(
        int,
        input("Enter first sorted array: ").split()
    ))

    # Read second array
    nums2 = list(map(
        int,
        input("Enter second sorted array: ").split()
    ))

    # Create Solution object
    obj = Solution()

    # Find median
    result = obj.findMedianSortedArrays(nums1, nums2)

    # Display result
    print("Median:", result)
