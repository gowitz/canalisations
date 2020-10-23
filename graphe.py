#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import math
from pprint import pprint

import matplotlib.pyplot as plt
from geojson import Feature, Point

with open('points_sample.geojson') as f:
    dataP = json.load(f)

with open('troncons_sample.geojson') as f:
    dataT = json.load(f)

#data = json.load(open('chambres.json'))

# Section declaration-----------------------------------------------------------

trace = ["G", "H", "C"]
coord_x = []
coord_y = []

# function calculLongueur


def calculLongueur(sp, ep):
    """
        Calculate distance between sp and ep

        :param sp: starting point number
        :param ep: ending point number
        :type pd: string
        :type pa: string
        :return: distance between sp and ep
        :rtype: float
    """
    d = getPointGeometry(sp)
    a = getPointGeometry(ep)
    return math.sqrt(((d[0] - a[0]) ** 2) + ((d[1] - a[1]) ** 2))

# function calculLongueur


def calculLongueurByGeometry(sp, ep):
    """
        Calculate distance between sp and ep

        :param sp: coordinates starting point
        :param ep: coordinates ending point
        :type sp: list
        :type ep: list
        :return: distance between sp and ep
        :rtype: float
    """
    return math.sqrt(((sp[0] - ep[0]) ** 2) + ((sp[1] - ep[1]) ** 2))

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
    for feature in dataP['features']:
        if no == feature['properties']['NO']:
            coord = feature['geometry']['coordinates']
            break
    return coord

# function calculePente


def calculPente(sp, ep):
    """
        La fonction retourne la pente en % entre les points passes en argument

        :param sp: start point number
        :param ep: end point number
        :type sp: string
        :type en: string
        :return: pente entre pd et pa en %
        :rtype: float
    """
    d = getPointGeometry(sp)
    a = getPointGeometry(ep)
    return (d[2] - a[2]) / calculLongueur(sp, ep) * 100

# function getLine


def getLine(id):
    """
        La fonction retourne la geometrie de la ligne selon ID passé en argument

        :param id: ID de la ligne
        :type id: integer
        :return: geometrie de la ligne
        :rtype: list
    """
    line = []
    for feature in dataT['features']:
        if id == feature['properties']['id']:
            line = feature['geometry']['coordinates']
            break
    return line

# function getLineWidth


def getLineWidth(line):
    """
        La fonction retourne la longueur d'une ligne passée en argument

        :param line: geometrie de la ligne
        :type line: list
        :return: longueur de la ligne
        :rtype: float
    """
    lineWidth = 0
    if len(line) > 1:
        for s in range(len(line)-1):
            sp = line[s]
            ep = line[s+1]
            lineWidth += calculLongueurByGeometry(sp, ep)

    return lineWidth

# function getSegments


def getSegments(axis):
    """
        La fonction retourne toutes les coordonnes de l'axe passé en argument

        :param axis: x or y
        :type axis: string
        :return: listing de coodonnees de l'axe
        :rtype: list
    """
    if axis.upper() == "X":
        i = 0
    else:
        i = 1

    c = []
    for feature in dataT['features']:
        coord = feature['geometry']['coordinates']
        for s in coord:
            c.append(s[i])

    return c


# Section tests ----------------------------------------------------------------

print("=== TEST functions ===")
print(
    "coordinates for point A expect [ 2552540.625519244465977, 1197882.251005402067676 ]")
print("-->  : ", getPointGeometry(trace[0]))
print("calculate distance between A and B")
print(round(calculLongueur("A", "B"), 2), "m")
print("calculate slope between A and B")
print(round(calculPente("A", "B"), 2), "%")

print(type(getPointGeometry(trace[0])))

print("=== Line ===")
print("Multi segments line width :", round(getLineWidth(getLine(9)), 2), "m")
print("Single segments line (A to B) width :",
      round(getLineWidth(getLine(1)), 2), "m")


"""
for chambre in data:
    n = chambre.get("no")
    if n == "72":
        x = chambre.get("X")
        y = chambre.get("Y")
        print("%s - %s / %s" %  (n, x, y))

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
# plt.xlabel('Distance')
# plt.ylabel('Altitude')
#plt.axis([80, 180, 1, 10])

for feature in dataP['features']:
    no = feature['properties']['NO']
    coord = feature['geometry']['coordinates']
    coord_x.append(coord[0])
    coord_y.append(coord[1])
    plt.text(coord[0], coord[1], no)

x = getSegments("X")
y = getSegments("Y")
plt.grid(True)
plt.plot(coord_x, coord_y, "o")
plt.plot(x, y)
plt.grid(True)
plt.show()
