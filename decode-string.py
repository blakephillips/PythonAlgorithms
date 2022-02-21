# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        currentString = ""
        decodedString = ""
        currentMultiplier = ""


        #For every character in the string
        for c in s:
            #If it's a number, add to currentMultipler
            if c.isdigit():
                currentMultiplier += c

            #If opening of new expression, pop to countStack, stringStack
            elif c == "[":
                if len(currentMultiplier) == 0: currentMultiplier = "0"
                countStack.append(int(currentMultiplier))
                stringStack.append(currentString)

                currentMultiplier = ""
                currentString = ""

            #If expression closes, pop from stringStack and multiply
            elif c == "]":
                decodedString = stringStack.pop() + (currentString * countStack.pop())
                currentString = decodedString
                currentMultiplier = ""
            else:
                currentString += c

        return currentString

if __name__ == '__main__':

    s = "2[abc]3[cd]ef"
    solution = Solution()
    s = solution.decodeString(s)
    print(s)