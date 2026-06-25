class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += f'{len(s)}#{s}'
        return msg

    def decode(self, s: str) -> List[str]:
        msgs = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            msgs.append(s[j+1:j+1+length])
            i = j + 1 + length
        return msgs
