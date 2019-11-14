
file_to_backup = '../assets/text.txt'
file_backup_name = '../assets/text_bak.txt'

try:
    with open(file_to_backup, 'r', encoding='utf-8') as file_to_read, open(file_backup_name, 'w', encoding='utf-8') as file_backup:
        # Read the content of the file to backup and write it into the backup file
        content = file_to_read.readlines()

        # Write the line number into the backup file
        line_number = 1
        for line in content:
            file_backup.write(str(line_number) + ':' + line + '\n')
            line_number += 1
        print("Backup was successfully created at:", file_backup_name)

# Error handling
except FileNotFoundError:
    print("The file", file_to_backup, "could not be found")
except PermissionError:
    print("You do not have the right permissions")
except Exception:
    print("Well something went wrong")
