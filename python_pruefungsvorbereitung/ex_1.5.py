# a) Schreiben Sie ein Programm, dass nur die Zahlen ausgibt, die in beiden Listen vorhanden sind. Es sollen jedoch keine Duplikate vorkommen

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Variante 1
set_a = set(list_a)
set_b = set(list_b)

merged = list(set_b.intersection(set_a))
print(merged)


#Variante 2
"""
merged_list = []
for element_a in list_a:
	if element_a in list_b and element_a not in merged_list:
		merged_list.append(element_a)


for element_b in list_b:
	if element_b in list_a and not element_b in merged_list:
		merged_list.append(element_b)

print(merged_list)
"""

# b) Schreiben Sie ein Programm, dass nur die Zahlen ausgibt, die nur in der einen oder in der anderen Liste vorkommen.
"""
set_a = set(list_a)
set_b = set(list_b)

only_b = list(set_b.difference(set_a))
print(only_b)
"""