# -*- coding: UTF-8 -*-

import sys

'''
file1.txt
---------------
foo1 3 4
foo2 5 8
foo3 8 9

file2.txt
---------------
bar1 foo1
bar2 foo2

两个文件第1列和第2列相同，按照这2列合并输出
python3 merge.py file1.txt file2.txt 1 2
---------------
foo1 3 4 bar1 foo1
foo2 5 8 bar2 foo2
foo3 8 9
'''

file1 = sys.argv[1]
file2 = sys.argv[2]
idx1 = int(sys.argv[3]) - 1
idx2 = int(sys.argv[4]) - 1

def read_file(filename):
    f = open(filename, "r")
    line_list = []

    while True:
        line = f.readline().strip()
        if not line:
            break
        line_list.append(line)
    f.close()
    return line_list

line_list_1 = read_file(file1)
line_list_2 = read_file(file2)
merge_result = {}

for line in line_list_1:
    columns = line.split()
    key1 = columns[idx1]
    merge_result[key1] = [line, ""]

for line in line_list_2:
    columns = line.split()
    key2 = columns[idx2]
    if merge_result.get(key2, None) is not None:
        merge_result[key2][1] = line
    else:
        merge_result[key2] = ["", line]

for key in merge_result:
    print(merge_result[key][0] + "\t" + merge_result[key][1])
