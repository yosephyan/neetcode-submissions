class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1
        one = 1
        while one:
            if length >= 0:
                if digits[length] == 9:
                    digits[length] = 0
                else:
                    digits[length] = digits[length] + 1
                    one = 0
            else:
                digits.insert(0, one)
                one = 0
            length -= 1
        return digits