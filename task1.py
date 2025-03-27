class Solution:
    def intToRoman(self, num):
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        result = []

        for value, symbol in roman_numerals:
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)


# Example usage:
solution = Solution()
print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(solution.intToRoman(58))  # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV"
