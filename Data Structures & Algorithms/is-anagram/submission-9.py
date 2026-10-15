class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = [0] * 26
        t_dict = [0] * 26

        for charS in s:
            s_dict[ord(charS) - ord("a")] += 1

        for charT in t:
            t_dict[ord(charT) - ord("a")] += 1

        return s_dict == t_dict
