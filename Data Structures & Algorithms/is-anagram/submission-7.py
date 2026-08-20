class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string = []
        t_string = []
        for schar in s:
            s_string.append(schar)
        for tchar in t:
            t_string.append(tchar)
        s_string.sort()
        t_string.sort()
        if s_string == t_string:
            return True

        return False