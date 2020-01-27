# @Author Xincheng Shen
# for CSE 120 pa2
from __future__ import print_function
import sys

argv = sys.argv
if len(argv) == 1:
    print('Usage: python timespread.py <the result of your program>\n\n'
          'To generate the result of your program:\n'
          '  for thread i (0 <= i <= 9)\n'
          ' - Whenever you enter a process i, DPrint "si" (for example, "s1")\n'
          ' - SlowPrintf the "iiiiiiiiiiiiiiii" (the more the better) \n'
          ' - Whenever you exit a process i, DPrint "ei"'
          )
    exit(1)
cnt = 0
occurs = [0 for _ in range(10)]

print('0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t')
i = 0
while i < len(argv[1]):
    c = argv[1][i]

    if c.isdigit():
        occurs[int(c)] += 1
        cnt += 1
    else:
        if cnt > 0:
            for p in range(10):
                print(round(100*occurs[p]/cnt,2), end='\t')
            print()
            cnt = 0
            occurs = [0 for _ in range(10)]

        i+=1
        if c == 's':
            print('entering p'+argv[1][i] + ', ' + str(int(cnt)) +' chars printed')
        if c == 'e':
            print('exiting  p'+argv[1][i] + ', ' + str(int(cnt)) +' chars printed')

    i += 1
