import os

folders_to_skip = ['.git', 'TEMP', 'SETUP']  # add more as needed

for folder, subfolders, filenames in os.walk('.'):
    for subfolder in folders_to_skip:
        if subfolder in subfolders:
            subfolders.remove(subfolder)

    for filename in filenames:
        if filename.endswith('.txt'):
            file_path = os.path.join(folder, filename)
            # tasks? open file and search, move/delete file, modify file
            # save name to a list, etc etc
            file_size = os.path.getsize(file_path)
            print(f"{file_size:8d} {os.path.abspath(file_path)}")
