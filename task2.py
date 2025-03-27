class Solution:
    def isValid(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                # Pop from stack if there's a match, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                if top_element != bracket_map[char]:
                    return False
            else:
                stack.append(char)

        return not stack  # Stack should be empty for a valid string

# Example usage:
solution = Solution()
print(solution.isValid("()"))       # Output: True
print(solution.isValid("()[]{}"))   # Output: True
print(solution.isValid("(]"))       # Output: False
print(solution.isValid("([])"))     # Output: True
