class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        ans = {}

        for x in nums2:
            while stack and x > stack[-1]:
                ans[stack.pop()] = x
            stack.append(x)
        return [ans.get(x, -1) for x in nums1]