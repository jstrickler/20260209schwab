import fileinput
from argparse import ArgumentParser
import re

parser = ArgumentParser(description="Faux Grep")

parser.add_argument('-i', dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument('-f', dest="show_file_names", action="store_true", help="show file name")
parser.add_argument('search_term', help="search term to find")
parser.add_argument('file_list', nargs="*", help="Files to search")

args = parser.parse_args()

search_re = re.compile(args.search_term, re.IGNORECASE if args.ignore_case else 0)

for raw_line in fileinput.input(args.file_list):
    if search_re.search(raw_line):
        if args.show_file_names:
            print(fileinput.filename(), end=" ")
        print(raw_line.rstrip())
