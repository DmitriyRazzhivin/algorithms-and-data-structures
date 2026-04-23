class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        int_number = 0
        
        for i in range(len(s) - 1):
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                int_number -= roman_map[s[i]]
            else:
                int_number += roman_map[s[i]]
        
        int_number += roman_map[s[-1]]

        return int_number

            