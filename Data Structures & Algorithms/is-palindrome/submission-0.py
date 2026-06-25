class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum()).lower()

        length = len(cleaned)
        front = cleaned[:length // 2]
        back = cleaned[length // 2:] if length % 2 == 0 else cleaned[length // 2 + 1:]
        print(front)
        print(back)
        return front == back[::-1]