



from os import stat


def checker (s):
        pair = { ")":"(" ,"}":"{" ,"]":"[" }
        stack = []

        for ch in s:
                if ch in pair:
                        if stack and stack[-1] == pair[ch]:
                                stack.pop()
                        else:
                                return False
                else:
                    stack.append(ch)
        return len(stack) == 0

print(checker("[({}]"))