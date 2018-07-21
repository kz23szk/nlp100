#!/Users/kzfm/.pyenv/shims/python 
import sys

args = sys.argv

if len(args)!=3:
    print("""This program is required 2 argments!""")
else:
    with open(args[2], 'r') as f:
        line_list = f.readlines()
        len_list = len(line_list)
        N = int(args[1])
        for i in range(N):
            print(line_list[len_list-N+i], end="")
