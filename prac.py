print("Hello World")

# Comment

'''
Multi-line comment
'''

name = "Harry"
print(name)

# Data types

# Numbers
# Strings
# Lists
# Tuples
# Dictionaries (maps)

# Arithmetic operators
# + - * / % ** //

print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

quote = "\"Always remember you are unique\""
print(quote)

multi_line_quote = '''just
like everyone else''' # template string
print(multi_line_quote)

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

print('\n' * 5)

print("I don't like ", end="")
print("newlines")