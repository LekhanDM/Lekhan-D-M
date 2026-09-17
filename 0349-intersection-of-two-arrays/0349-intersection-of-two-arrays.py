class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)
        answer = []

        for x in nums2:
            if x in seen:
                answer.append(x)
                seen.remove(x)
        return answer