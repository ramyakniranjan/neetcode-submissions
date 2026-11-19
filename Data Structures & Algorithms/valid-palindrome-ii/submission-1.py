class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        def is_palindrome_range(left:int ,right: int) -> bool:
            while left < right:
                if not s[left].isalnum():
                    left += 1
                elif not s[right].isalnum():
                    right -= 1
                elif s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] != s[right]:
                return is_palindrome_range(left+1,right) or is_palindrome_range(left,right - 1)
            left += 1
            right -= 1
        return True
      

        