"""print size of every python file whose name starts with "m" """

import os

START_DIR = ".."  # start in root of student files  # starting location


def main():
    for currdir, subdirs, files in os.walk(START_DIR):  # walk folder tree
        for file in files:  # loop over file names
            if file.endswith('.py') and file.startswith('m'):
                fullpath = os.path.join(currdir, file)  # get file path
                fsize = os.path.getsize(fullpath)
                print(f"{fsize:8d} {fullpath:s}")


if __name__ == '__main__':
    main()
