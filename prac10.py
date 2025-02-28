long_string = "This is a very long string that I am going to use to demonstrate how to split a string into a list of words."

print(long_string[0:4]) # first four characters
print(long_string[-6:]) # last six characters
print(long_string[:-6]) # all but the last six characters
print(long_string[:4] + " is awesome") # first four characters + " is awesome"

print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))