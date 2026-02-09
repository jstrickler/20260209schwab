import os

path = os.getenv('PATH')
paths = path.split(os.pathsep)

for path_dir in paths:
    if os.path.exists(path_dir):
        all_files = os.listdir(path_dir)
        print(f"{path_dir}: {len(all_files)}")
    else:
        print(f"WARNING: {path_dir} is in PATH, but does not exist")
