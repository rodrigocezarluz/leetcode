"""
Problem: LeetCode 20 - Valid Parentheses

Key Idea:
To determine if a given string of parentheses 's' is valid, we can use a stack data structure. We iterate through each character in 's', and if the character is an opening parenthesis ('(', '{', '['), we push it onto the stack. If the character is a closing parenthesis (')', '}', ']'), we check if the stack is empty or if the top element of the stack does not match the current closing parenthesis. If either of these conditions is met, we know the string is not valid. Otherwise, we pop the top element from the stack. At the end, if the stack is empty, the string is valid.

Time Complexity:
The time complexity of this solution is O(n), where n is the length of the input string 's'. We iterate through the string once, and each operation (pushing or popping from the stack) takes constant time.

Space Complexity:
The space complexity is O(n), where n is the length of the input string 's'. In the worst case, the stack could store all characters of the input string.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in parentheses_map:
                stack.append(c)
                continue
            if not stack or stack[-1] != parentheses_map[c]:
                return False
            stack.pop()

        return not stack


class MySolution:
    def isValid(self, s: str) -> bool:
        par_stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                par_stack.append(c)
            elif len(par_stack) > 0:
                if c == ")" and par_stack[-1] == "(":
                    par_stack.pop()
                elif c == "]" and par_stack[-1] == "[":
                    par_stack.pop()
                elif c == "}" and par_stack[-1] == "{":
                    par_stack.pop()
                else:
                    return False
            else:
                return False
        return len(par_stack) == 0


test = MySolution()
print(test.isValid("()"))  # Output: True
print(test.isValid("()[]{}"))  # Output: True
print(test.isValid("(]"))  # Output: False
print(test.isValid("([)]"))  # Output: False
