class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        j = 0
        for i in nums1:
            while j != len(nums2) and i > nums2[j]:
                j += 1
            nums2.insert(j, i)
        n = len(nums2)
        if n % 2:
            return nums2[n // 2]
        return (nums2[n // 2] + nums2[n // 2 - 1]) / 2
