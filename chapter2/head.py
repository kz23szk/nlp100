#!/Users/kzfm/.pyenv/shims/python 
import sys

args = sys.argv

if len(args)!=3:
    print("""This program is required 2 argments!""")
else:
    with open(args[2], 'r') as f:
        count = int(args[1])
        for line in f:
            print(line, end="")
            count -= 1
            if count == 0:
                break
