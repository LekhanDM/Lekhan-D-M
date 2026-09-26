class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        a = b = None
        ca = cb = 0
        for x in nums:
            if x == a:
                ca += 1
            elif x == b:
                cb += 1
            elif ca == 0:
                a, ca = x, 1
            elif cb == 0:
                b, cb = x, 1
            else:
                ca -= 1
                cb -= 1
        ans = []
        for x in (a, b):
            if nums.count(x) > len(nums) // 3:
                ans.append(x)
        return ans
        