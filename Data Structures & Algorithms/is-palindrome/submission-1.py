class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum()).lower()

        front = 0
        back = len(cleaned) - 1

        while front < back:
            if cleaned[front] != cleaned[back]:
                return False
            front += 1
            back -= 1
        return True