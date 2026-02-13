import shlex
from glob import glob
from subprocess import run, PIPE, CalledProcessError
from pprint import pprint

# don't use os.system('cmd')

CMD = "netstat -an"
FILES = 'data/*.log'
FILE_LIST = glob(FILES)

CMD_WORDS = shlex.split(CMD)

print(f"{CMD_WORDS = }")

process = run(CMD_WORDS + FILE_LIST, stdout=PIPE)  # works on Windows, not on Mac/Linux
all_lines = process.stdout.decode().splitlines()
established_connections = [line for line in all_lines if 'ESTAB' in line and 'tcp4' in line]
pprint(established_connections)
