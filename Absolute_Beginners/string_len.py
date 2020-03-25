import string
A = input()
print(len(A.translate({ord(c): None for c in string.whitespace})))