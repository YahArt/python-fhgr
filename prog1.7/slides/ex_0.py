
with open('../assets/text.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

    # Print each line of the file
    line_number = 1
    for line in content:
        print('Zeile', line_number, ':', line)
        line_number +=1

    # Print only the 4th line
    print('Zeile', 4, ':', content[3])
