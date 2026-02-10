import os  # includes os.path
from datetime import datetime

print(f"{os.getuid() = }")
print(f"{os.getpid() = }")
os.makedirs('foo/bar/blah', exist_ok=True)

FOLDER = "DATA"
FILENAME = "mary.txt"

file_path = os.path.join(FOLDER, FILENAME)
print(f"{file_path = }")
print(f"{os.path.dirname(file_path) = }")
print(f"{os.path.basename(file_path) = }")
print(f"{os.path.abspath(file_path) = }")
print(f"{os.path.getmtime(file_path) = }")
print(f"{os.path.getatime(file_path) = }")
raw_timestamp = os.path.getmtime(file_path)
timestamp = datetime.fromtimestamp(raw_timestamp)
print(f"{timestamp = }")
print(f"{os.path.getsize(file_path) = }")
print(f"{os.path.exists(file_path) = }")
print(f"{os.path.exists('wombats.txt') = }")
print(f"{os.path.split(file_path) = }")
print(f"{os.path.splitext(file_path) = }")
print('-' * 60)

print(f"{os.listdir('DATA') = }")

for item in os.scandir('DATA'):
    print(item.name, item.is_dir(), item.is_file(), oct(item.stat().st_mode))
