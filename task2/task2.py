import sys
import math
strc1 = sys.argv[1]
strc2 = sys.argv[2]
def func(*args):
    fname = open(strc1, 'r')
    flst = [line.split() for line in fname]
    fname.close()
    cname = open(strc2, 'r')
    coordlist = [line.split() for line in cname]
    cname.close()
    Alst = []
    Blst = []
    for i in range (0, 2):
        Blst.append(0)
        i += 1
    Clst = []
    for i in range (0, 2):
        Clst.append(0)
        i += 1
    Dlst = []
    for i in range (0, 2):
        Dlst.append(0)
        i += 1
    for i in range (0, 2):
        Alst.append(0)
        i += 1
    for i in range(0, 2):
        for j in range(0, 1):
            Alst[i] = float(flst[j][i])
    for i in range(0, 2):
        for j in range(1,2):
            Blst[i] = float(flst[j][i])
    for i in range(0, 2):
        for j in range(2,3):
            Clst[i] = float(flst[j][i])
    for i in range(0, 2):
        for j in range(3,4):
            Dlst[i] = float(flst[j][i])
    dotcorlist = [[0] * 2 for i in range(len(coordlist))]

    for i in range (0, len(coordlist)):
        for j in range(0, 2):
               dotcorlist[i][j] = float(coordlist[i][j])
    for i in range(0, len(dotcorlist)):
        if(dotcorlist[i] == Alst) or (dotcorlist[i] == Blst) or (dotcorlist[i] == Clst) or (dotcorlist[i] == Dlst):
            print(0)
        elif((Alst[0] < dotcorlist[i][0] < Blst[0] and ((dotcorlist[i][0] - Alst[0]) * (Blst[1]-Alst[1]) - (dotcorlist[i][1]-Alst[1])*(Blst[0]-Alst[0] == 0))
            or
                (Blst[0] < dotcorlist[i][0] < Alst[0] and (((dotcorlist[i][0] - Alst[0]) * (Blst[1]-Alst[1])) - ((dotcorlist[i][1]-Alst[1])*(Blst[0]-Alst[0] == 0)))
            or
                (Blst[0] < dotcorlist[i][0] < Clst[0] and (((dotcorlist[i][0] - Blst[0]) * (Clst[1]-Blst[1])) - ((dotcorlist[i][1]-Blst[1])*(Clst[0]-Blst[0]) == 0)))
            or
                (Clst[0] < dotcorlist[i][0] < Blst[0] and (((dotcorlist[i][0] - Blst[0]) * (Clst[1]-Blst[1])) - ((dotcorlist[i][1]-Blst[1])*(Clst[0]-Blst[0]) == 0)))
            or
                (Clst[0] < dotcorlist[i][0] < Dlst[0] and (((dotcorlist[i][0] - Clst[0]) * (Dlst[1]-Clst[1])) - ((dotcorlist[i][1]-Clst[1])*(Dlst[0]-Clst[0]) == 0)))
            or
                (Dlst[0] < dotcorlist[i][0] < Clst[0] and (((dotcorlist[i][0] - Clst[0]) * (Dlst[1]-Clst[1])) - ((dotcorlist[i][1]-Clst[1])*(Dlst[0]-Clst[0]) == 0)))
            or
                (Alst[0] < dotcorlist[i][0] < Dlst[0] and (((dotcorlist[i][0] - Dlst[0]) * (Alst[1]-Dlst[1])) - ((dotcorlist[i][1]-Dlst[1])*(Alst[0]-Dlst[0]) == 0)))
            or
                (Dlst[0] < dotcorlist[i][0] < Alst[0] and ((dotcorlist[i][0] - Dlst[0]) * (Alst[1]-Dlst[1]) - ((dotcorlist[i][1]-Dlst[1])*(Alst[0]-Dlst[0]) == 0)))
        ))):
            print(1)
        elif ((min(Alst[0], Blst[0])) < (dotcorlist[i][0])
                and
                ((max(Clst[0], Dlst[0])) > (dotcorlist[i][0]))
                and
                ((min(Alst[0], Dlst[1])) < dotcorlist[i][1])
                and
                ((max(Blst[1], Clst[1]) > dotcorlist[i][1]))):
            print(2)
        else:
            print(3)

func(strc1, strc2)
