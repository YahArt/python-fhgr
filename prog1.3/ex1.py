list = ['larry', 'curly', 'moe']

# Add shemp to the end
list.append("shemp")
print(list)

# Add "xxx" at index 0
list.insert(0, "xxx")
print(list)

# Add the list ['yyy', 'zzz'] at the end
list.extend(['yyy', 'zzz'])
print(list)

# Search and remove 'curly'
list.remove('curly')
print(list)