import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        return json.dumps([[ord(c) for c in s] for s in strs])

    def decode(self, s: str) -> List[str]:
        strs = json.loads(s)
        return ["".join([chr(c) for c in s]) for s in strs]
