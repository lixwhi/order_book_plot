import csv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timezone
from web3 import Web3
import json
gree = "#74e54760"
ree = "#e5475460"
CIRC_SCALAR = 10000
DAIMETER_MAX = 100000
DAIMETER_MIN = 250
INNER_LIQUID_LINE = 10000
OUTER_LIQUID_LINE = 50000

filename ='7214010-7218246_20190213-small.csv'
outfile = '7214010-7218246_20190213.png'
x = np.loadtxt(open(filename, "rb"), delimiter=",", skiprows=1, usecols=0)
y = np.loadtxt(open(filename, "rb"), delimiter=",", skiprows=1, usecols=1)
s = np.loadtxt(open(filename, "rb"), delimiter=",", skiprows=1, usecols=2)
boa = np.loadtxt(open(filename, "rb"), delimiter=",", skiprows=1, usecols=3)
c = np.empty(boa.size, dtype=np.dtype(('U10', 1)))
c[boa == 1] = gree
c[boa == -1] = ree

s[s > DAIMETER_MAX] = DAIMETER_MAX
s[s < DAIMETER_MIN] = DAIMETER_MIN
s = s / DAIMETER_MIN
s = np.square(s)
# now 0-1
s = s / ((DAIMETER_MAX / DAIMETER_MIN) ** 2)
s = s * CIRC_SCALAR

fig = plt.figure()
ax1 = plt.axes()
ax1.set_ylim(115, 132)
plt.scatter(x, y, s=s, c=c, marker="|")
plt.title('Oasis book ' + outfile)
ax1.set_xlabel('blocks')
ax1.set_ylabel('WETH/DAI')
#plt.savefig(outfile, dpi=2000)
plt.show()