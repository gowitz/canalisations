#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *
import matplotlib.pyplot as plt
import json
from geojson import Feature, Point
from pprint import pprint

with open('points_sample.geojson') as f:
    data = json.load(f)

#data = json.load(open('chambres.json'))

# Section declaration-----------------------------------------------------------

trace = ["G", "H", "C"]
coord_x = []
coord_y = []

# function calculLongueur
def calculLongueur(pd, pa):
    """
        La fonction retourne distance entre les points passes en argument

        :param pd: no point depart
        :param pa: no point arrivee
        :type pd: string
        :type pa: string
        :return: distance entre pd et pa
        :rtype: float
    """
    d = getPointGeometry(pd)
    a = getPointGeometry(pa)
    return round(sqrt(((d[0] - a[0]) ** 2) + ((d[1] - a[1]) ** 2)),2)

# Section fonctions ------------------------------------------------------------

# function getPointGeometry
def getPointGeometry(no):
    """
        La fonction retourne les coodonnees du point passe en argument

        :param no: no point
        :type pd: string
        :return: coordonnes point
        :rtype: list
    """
    for feature in data['features']:
        if no == feature['properties']['NO']:
            coord = feature['geometry']['coordinates']
            break
    return coord

# Section tests ----------------------------------------------------------------

print "=== TEST functions ==="
print "coordinates for point A expect [ 2552540.625519244465977, 1197882.251005402067676 ]"
print "-->  : ", getPointGeometry(trace[0])
print "calculte distance between A and B"
print calculLongueur("A", "B"), "m"

print type(getPointGeometry(trace[0]))


"""
for chambre in data:
    n = chambre.get("no")
    if n == "72":
        x = chambre.get("X")
        y = chambre.get("Y")
        print "%s - %s / %s" %  (n, x, y)

#pprint(data)
"""

# Section graphe ---------------------------------------------------------------

"""
plt.plot([542665.593,542627.071,542674.80],[151723.232,151711.858,151707.27], "o")
plt.text(542665.593, 151723.232, '44')
plt.text(542627.071, 151711.858, '43A')
plt.text(542674.80, 151707.27, '45')
"""
#plt.annotate('45', xy=(542674.80, 151707.27), xytext=(542674.80, 151707.5))

#plt.title("Profil en long")
#plt.plot([50,100,150,200], [1,2,3,4])
#plt.xlabel('Distance')
#plt.ylabel('Altitude')
#plt.axis([80, 180, 1, 10])

for feature in data['features']:
    no = feature['properties']['NO']
    coord = feature['geometry']['coordinates']
    coord_x.append(coord[0])
    coord_y.append(coord[1])
    plt.text(coord[0], coord[1], no)


plt.grid(True)
plt.plot(coord_x, coord_y, "o")
plt.grid(True)
plt.show()
