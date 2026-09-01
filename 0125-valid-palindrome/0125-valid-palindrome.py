class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        h = s.lower()
        while left < right:
            
            if not h[left].isalnum():
                left+=1
                continue
            if not h[right].isalnum():
                right -= 1
                continue
            if h[left] != h[right]:
                return False
            left+=1
            right-=1
        return True