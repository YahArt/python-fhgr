
# Note that we have a list with some nested elements
# 1. character
# 2. tuple (constant list) which itself contains two strings
# 3. another list
random = ['a', ('b', 'cd'), [3, 4]]

# [3, 4]
print(random[2])

# a
print(random[0])

# 4
print(random[2][1])

# b
print(random[1][0])

# d (taken from 'cd' via range slicing)
print(random[1][1][-1])

# 'cd'
print(random[1][1])