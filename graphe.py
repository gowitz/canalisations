#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import json
from pprint import pprint

data = json.load(open('chambres.json'))

plt.plot([542665.593,542627.071,542674.80],[151723.232,151711.858,151707.27], "o")
plt.text(542665.593, 151723.232, '44')
plt.text(542627.071, 151711.858, '43A')
plt.text(542674.80, 151707.27, '45')
#plt.annotate('45', xy=(542674.80, 151707.27), xytext=(542674.80, 151707.5))

#plt.title("Profil en long")
#plt.plot([50,100,150,200], [1,2,3,4])
#plt.xlabel('Distance')
#plt.ylabel('Altitude')
#plt.axis([80, 180, 1, 10])
plt.grid(True)
#plt.show()

trace = ["74", "42", "12A"]


for chambre in data:
    n = chambre.get("no")
    if n == "72":
        x = chambre.get("X")
        y = chambre.get("Y")
        print "%s - %s / %s" %  (n, x, y)

#pprint(data)