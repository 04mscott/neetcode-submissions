class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += f'{len(s)}#{s}'
        return msg

    def decode(self, s: str) -> List[str]:
        msgs = []
        word_len = 0
        curr_msg = ""
        i = 0
        while i < len(s):
            if word_len == 0 and len(s) > i + 1:
                str_len = ""
                while s[i] != '#':
                    str_len += s[i]
                    i += 1
                word_len = int(str_len)
                i += 1

            while word_len > 0:
                curr_msg += s[i]
                i += 1
                word_len -= 1
            
            msgs.append(curr_msg)
            curr_msg = ""

        return msgs

