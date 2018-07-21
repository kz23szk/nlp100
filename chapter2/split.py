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
        for i in range(len_list//N):
            with open(str(i) + '.txt', 'w') as f:
                f.write("".join(line_list[i*N:(i+1)*N]))
        else:
            num = i+1
        with open(str(num) + '.txt', 'w') as f:
            f.write("".join(line_list[N * num:]))

