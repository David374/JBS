import sys
import math
strc1 = sys.argv[1]
def func(*args):
    cash1f = open(strc1 + "\Cash1.txt", 'r')
    cash1_lst = [float(i) for i in cash1f]
    cash1f.close()
    cash2f = open(strc1 + "\Cash2.txt", 'r')
    cash2_lst = [float(i) for i in cash2f]
    cash2f.close()
    cash3f = open(strc1 + "\Cash3.txt", 'r')
    cash3_lst = [float(i) for i in cash3f]
    cash3f.close()
    cash4f = open(strc1 + "\Cash4.txt", 'r')
    cash4_lst = [float(i) for i in cash4f]
    cash4f.close()
    cash5f = open(strc1 + "\Cash5.txt", 'r')
    cash5_lst = [float(i) for i in cash5f]
    cash5f.close()
    sfdocker = []
    for i in range (0, 16):
        sfdocker.append(0)
    for i in range(0, 16):
        sfdocker[i] += cash1_lst[i] + cash2_lst[i] + cash3_lst[i] + cash4_lst[i] + cash5_lst[i]
        i = i + 1
    print(sfdocker.index(max(sfdocker)) + 1)

func(strc1)

