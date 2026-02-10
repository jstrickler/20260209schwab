import os

# Prompt user for Directory input
dir = input("Please enter a directory: ")  # or sys.argv[1]
if os.path.isdir(dir):
    oldest_file = None
    oldest = 9999999999999
    for dir_entry in os.scandir(dir):
        if not dir_entry.is_file():
            break
        file_path = os.path.join(dir, dir_entry.name)
        if os.path.isfile(file_path):
            timestamp = os.path.getmtime(file_path)
            if timestamp < oldest:
                oldest_file = dir_entry.name
                oldest = timestamp 
    print(oldest_file)
else:
    print("Directory does not exist.")