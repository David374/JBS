import sys
import math
str = sys.argv[1]
def func(*args):
    file_name = open(str, 'r')
    lst = [int(i) for i in file_name]
    srtlst = [int(i) for i in sorted(lst)] #отсортированный список
    lstsize = len(srtlst) #размер списка
    rang = 1 + ((90 * (lstsize - 1))/100) #ранг
    dint = rang - int(rang) # дробная часть
    rang = math.floor(rang) #ранг
    percentile = srtlst[rang-1] + dint * (srtlst[rang] - srtlst[rang-1])
    print("%.2f" % percentile) #вывод 90перцентиля
    if (lstsize % 2 == 0):
        median = ((srtlst[lstsize // 2] + srtlst[(lstsize // 2) - 1]) // 2)
        print("%.2f" % median)
    elif lstsize % 2 != 0:
        median = srtlst[(lstsize - 1) // 2]
        print("%.2f" % median)
    print("%.2f" % max(srtlst))
    print("%.2f" % min(srtlst))
    print("%.2f" % (sum(srtlst) / lstsize))
    file_name.close()

func(str)

