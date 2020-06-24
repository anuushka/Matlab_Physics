import math
import numpy as np

import matplotlib.pyplot as plt

def Get_data(Path1):
    with open(Path1) as f:
        data_ = f.readlines()[9:]
        
    data1 = []
    for i in data_:
        x, y, v = i.split()
        x, y = float(x), float(y)
        v = complex(v.replace('i', 'j')).real

        data1.append([x, y, v])
    return data1

def E(x, y, data):
    return math.sqrt(find_P(x, y, data, 0) ** 2 + find_P(x, y, data, 1) ** 2)

def lenP(d, x, y):
    return math.sqrt((d[0] - x) ** 2 + (d[1] - y) ** 2)

def find_P(x, y, data, typ = 0): # typ = 0 means x, typ = 1 means y
    if typ:
        minP = min([i for i in data if i[typ] < y], key = lambda d: lenP(d, x, y))
        maxP = min([i for i in data if i[typ] > y], key = lambda d: lenP(d, x, y))
    else:
        minP = min([i for i in data if i[typ] < x], key = lambda d: lenP(d, x, y))
        maxP = min([i for i in data if i[typ] > x], key = lambda d: lenP(d, x, y))

    return (maxP[2] - minP[2]) / (maxP[typ] - minP[typ])

for part in range(1, 4):
    for d in range(1, 7):
        Path  = f'./lab 3.1/part{part}/{part}.{d}.txt'
        data1 = Get_data(Path)
        minX, maxX = min(data1, key = lambda x: x[0])[0], max(data1, key = lambda x: x[0])[0]
        minY, maxY = min(data1, key = lambda x: x[1])[1], max(data1, key = lambda x: x[1])[1]
        x = np.linspace(minX + 0.1, maxX -0.1, int((maxX - minX) * 10) - 2)
        y = np.linspace(minY + 0.1, maxY -0.1, int((maxY - minY) * 10) - 2)
        A1, res = [], []
        for i in x:
            cur = []
            for j in y:
                z = E(i, j, data1)
                res.append(z)
                cur.append(z)
            A1.append(cur)
        Z = np.array(A1)
        res = np.array(res)
        graph = plt.contourf(x, y, Z.T,
                                np.linspace(np.percentile(res, 25), np.percentile(res, 75), 200),
                                linestyle=None, extend='both',
                               cmap = 'coolwarm')
        plt.colorbar(graph)
        for c in graph.collections:
            c.set_edgecolor("face")

        plt.savefig(f'./lab 3.1/part{part}/{part}.{d}.png')
        plt.clf()