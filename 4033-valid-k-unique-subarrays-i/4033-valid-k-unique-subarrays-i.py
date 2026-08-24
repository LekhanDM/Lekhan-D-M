class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)

        block = int(n ** 0.5)

        merovlanti = nums

        # [left, right, query_index]

        q = []

        for i in range(len(queries)):

            l, r = queries[i]

            q.append([l, r, i])

        q.sort(key=lambda x: (x[0] // block, x[1]))

        freq = [0] * (100001)

        ans = [False] * len(queries)

        left = 0

        right = -1

        distinct = 0

        odd = 0

        for l, r, idx in q:

            while right < r:

                right += 1

                x = nums[right]

                if freq[x] == 0:

                    distinct += 1

                if freq[x] % 2 == 0:

                    odd += 1

                else:

                    odd -= 1

                freq[x] += 1

            while right > r:

                x = nums[right]

                if freq[x] % 2 == 1:

                    odd -= 1

                else:

                    odd += 1

                freq[x] -= 1

                if freq[x] == 0:

                    distinct -= 1

                right -= 1

            while left < l:

                x = nums[left]

                if freq[x] % 2 == 1:

                    odd -= 1

                else:

                    odd += 1

                freq[x] -= 1

                if freq[x] == 0:

                    distinct -= 1

                left += 1

            while left > l:

                left -= 1

                x = nums[left]

                if freq[x] == 0:

                    distinct += 1

                if freq[x] % 2 == 0:

                    odd += 1

                else:

                    odd -= 1

                freq[x] += 1

            if distinct == k and odd == 0:

                ans[idx] = True

        return ans