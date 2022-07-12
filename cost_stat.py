#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import re

f = open(sys.argv[1], "r")
lines = f.read().strip().split("\n")
ct = []
qps = 0
for line in lines:
    if line.strip() == "":
        continue
    cost = float(line.strip())
    ct.append(cost/1000)
a=np.array((ct))
np.median(a)

print "平均\t90分位\t95分位\t99分位\t最慢"
print str(np.mean(a)) + "ms\t"+ str(np.percentile(a, 90))+ "ms\t"+ \
        str(np.percentile(a, 95))+ "ms\t"+ str(np.percentile(a, 99))+ "ms\t" + str(np.max(a)) + "ms"
