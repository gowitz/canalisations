# -*- coding: utf-8 -*-
from math import *

class Point:

	def __init__(self, pid, x, y, z):
		self.pid = pid
		self.x = x
		self.y = y
		self.z = z

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getZ(self):
		return self.z

	def getID(self):
		return self.pid

	def info(self):
		print "ID : " + str(self.pid) + "\n" \
		      "X  : " + str(self.x) + "\n" \
		      "Y  : " + str(self.y) + "\n" \
		      "Z  : " + str(self.z)

class Chambre(Point):

	def __init__(self, pid, x, y, z):
		Point.__init__(self, pid, x, y, z)

	def info(self):
		print "ID : " + str(self.pid) + "\n" \
		      "X  : " + str(self.x) + "\n" \
		      "Y  : " + str(self.y) + "\n" \
		      "ZC : " + str(self.z[0])+ "\n" \
		      "ZR : " + str(self.z[1])+ "\n" \
		      "ZS : " + str(self.z[2])
		for i in range(len(self.z) - 3):
			print "ZE" + str(i+1) + ": "  + str(self.z[3+i])

	def getCC(self):
		return self.z[0]

	def getCR(self):
		return self.z[1]

	def getCS(self):
		return self.z[2]

	def getCE(self, e):
		if len(self.z) > 3 and 3 + e <= len(self.z):
			return self.z[2 + e]
		else:
			return

class Troncon():

	def __init__(self, chd, cha, e, diam, mat):
		self.chd = chd     # chambre depart [chambre]
		self.cha = cha     # chambre arrive [chambre]
		self.e = e         # entree dans chambre arrivee [integer]
		self.diam = diam   # diametre [integer]
		self.mat = mat     # materiaux [string]

	def getLongueur(self):
		return sqrt(((self.chd.getX() - self.cha.getX()) ** 2) + ((self.chd.getY() - self.cha.getY()) ** 2))

	def getPente(self):
		return (self.chd.getCS() - self.cha.getCE(self.e)) / self.getLongueur() * 100

	def getDiametre(self):
		return str(self.diam)

	def getMateriaux(self):
		return str(self.mat)

	def setDiametre(self, diam):
		self.diam = diam

	def setMateriaux(self, mat):
		self.mat = mat

	def getAngleTexte(self):
		deltaX = self.chd.getX() - self.cha.getX()
		deltaY = self.chd.getY() - self.cha.getY()

		if deltaX != 0:
			return atan( deltaY / deltaX ) / (2 * pi) * 360
		else:
			return 90

	def getSensEcoulement(self):
		if self.cha.getX() > self.chd.getX():
			return "d"

		elif self.cha.getX() == self.chd.getX() and self.cha.getY() > self.chd.getY():
			return "d"

		else:
			return "g"

	def info(self):
		longueur = ("%.2f" % self.getLongueur())
		pente = ("%.2f" % self.getPente())
		sens = self.getSensEcoulement()
		mat = self.getMateriaux()
		diam = self.getDiametre()
		prefixe = ''
		sufixe = ''
		if sens == 'd':
			sufixe = ' -->'
		else:
			prefixe = '<-- '

		print prefixe + mat + " ∅" + diam + " / L=" + longueur + "m / i=" + pente + "%" + sufixe


def calculLongueur(pd, pa):
	return sqrt(((pd.getX() - pa.getX()) ** 2) + ((pd.getY() - pa.getY()) ** 2))

def calculePente(pd, pa, e):
	return (pd.getCS() - pa.getCE(e)) / calculLongueur(pd, pa) * 100

def calculAngleTexte(pd, pa):
	deltaX = pd.getX() - pa.getX()
	deltaY = pd.getY() - pa.getY()

	if deltaX != 0:
		return atan( deltaY / deltaX ) / (2 * pi) * 360
	else:
		return 90
"""
def calculAngleTexte(pd, pa):
	a = calculeAngleDeg(pd, pa)
	if pa.getX() > pd.getX():
		if pa.getY() > pd.getY():
			at = a
		else:
			at = 360 - a
	else:
		if pa.getY() > pd.getY():
			at = 180 - a
		else:
			at = 180 + a

	if at > 90 and at <= 270:
		at = at-180

	return at
"""

def sensEcoulement(pd, pa):
	if pa.getX() > pd.getX():
		return "d"

	elif pa.getX() == pd.getX() and pa.getY() > pd.getY():
		return "d"

	else:
		return "g"

def infoTroncon(pd, pa, e):
	longueur = calculLongueur(pd, pa)
	pente = calculePente(pd, pa, e)
	sens = sensEcoulement(pd, pa)
	prefixe = ''
	sufixe = ''
	if sens == 'd':
		sufixe = ' -->'
	else:
		prefixe = '<-- '

	return prefixe + "L=" + str(round(longueur,3)) + "m / i=" + str(round(pente,2)) + "%" + sufixe

""" ****************************************************************************
    DATA
**************************************************************************** """

p1 = Point('ch1', 542665.593, 151723.232, 557.37)
p2 = Point('ch2', 542627.071, 151711.858, 558.12)

ch1 = Chambre('44', 542665.593, 151723.232, [0, 557.37, 557.37])
ch2 = Chambre('43A', 542627.071, 151711.858, [558.12, 556.57, 556.57, 558.12])
ch3 = Chambre('45', 542674.80, 151707.27, [558.73, 556.95, 556.95, 558.73])
ch4 = Chambre('71', 542240.29, 151638.15, [550.20, 547.99, 547.99, 548])
ch5 = Chambre('72', 542209.70, 151638.38, [549.89, 547.62, 547.62, 547.64])
ch6 = Chambre('74', 542203.31, 151643.88, [549.70, 547.50, 547.50, 547.66, 547.54])
ch7 = Chambre('93', 542191.71, 151668.17, [550.15, 548.35, 548.35, 549.03,548.4])
ch8 = Chambre('94', 542236.28, 151664.04, [551.30, 549.25, 549.25, 549.34, 549.34])
ch9 = Chambre('12A', 542326.06, 151638.34, [551.45, 549.27, 549.27, 551.45, 551.45])
ch10 = Chambre('12ext2', 542186.03, 151680.95, [553.56, 552.56, 552.56, 552.6])
ch11 = Chambre('12ext3', 542149.05, 151690.17, [555.17, 554.17, 554.17, 554.14])
ch12 = Chambre('12ext4', 542190.20, 151674.40, [553.42, 552.42, 552.42, 552.44])
ch13 = Chambre('12ext6', 542123.83, 151700.77, [0.00, 555.00, 555.00])
ch14 = Chambre('14A', 542328.11, 151667.21, [0.00, 550.73, 550.73])

ch100 = Chambre('100', 0, 0, [7, 5, 5])
ch101 = Chambre('101', 5, 0, [2, 0, 0, 0])
ch102 = Chambre('102', 5, 5, [2, 0, 0, 0])
ch103 = Chambre('103', 0, 5, [2, 0, 0, 0])
ch104 = Chambre('104', -5, 5, [2, 0, 0, 0])
ch105 = Chambre('105', -5, 0, [2, 0, 0, 0])
ch106 = Chambre('106', -5, -5, [2, 0, 0, 0])
ch107 = Chambre('107', 0, -5, [2, 0, 0, 0])
ch108 = Chambre('108', 5, -5, [2, 0, 0, 0])

troncons = []

troncons.append(Troncon(ch100, ch101, 1, 500, 'PVC'))
troncons.append(Troncon(ch100, ch102, 1, 400, 'PVC'))
troncons.append(Troncon(ch100, ch103, 1, 350, 'PVC'))
troncons.append(Troncon(ch100, ch104, 1, 315, 'PVC'))
troncons.append(Troncon(ch100, ch105, 1, 300, 'PVC'))
troncons.append(Troncon(ch100, ch106, 1, 250, 'PVC'))
troncons.append(Troncon(ch100, ch107, 1, 200, 'PVC'))
troncons.append(Troncon(ch100, ch108, 1, 150, 'PVC'))

""" ****************************************************************************
    TEST
**************************************************************************** """

print infoTroncon(ch100, ch101, 1) + '\t\t' + str(calculAngleTexte(ch100, ch101))
print infoTroncon(ch100, ch102, 1) + '\t\t' + str(calculAngleTexte(ch100, ch102))
print infoTroncon(ch100, ch103, 1) + '\t\t' + str(calculAngleTexte(ch100, ch103))
print infoTroncon(ch100, ch104, 1) + '\t\t' + str(calculAngleTexte(ch100, ch104))
print infoTroncon(ch100, ch105, 1) + '\t\t' + str(calculAngleTexte(ch100, ch105))
print infoTroncon(ch100, ch106, 1) + '\t\t' + str(calculAngleTexte(ch100, ch106))
print infoTroncon(ch100, ch107, 1) + '\t\t' + str(calculAngleTexte(ch100, ch107))
print infoTroncon(ch100, ch108, 1) + '\t\t' + str(calculAngleTexte(ch100, ch108))

troncons[7].setDiametre(500)
troncons[7].setMateriaux('PE')

for t in troncons:
	t.info()

ch100.info()

"""
longueur = calculLongueur(p1, p2)
pente = calculePente(p1, p2)
azi = calculeAngleDeg(p1, p2)
angleTexte = calculeAngleTexte(p1, p2)

p1.getInfo()
print
p2.getInfo()
print

print sensEcoulement(p1, p2) + "L=" + str(round(longueur,3)) + "m / i=" + str(round(pente,2)) + "%"
print azi
print angleTexte
print
ch1.getInfo()
print
ch2.getInfo()
print "CH : " + ch1.getID() + " CC : " + str(ch1.getCC())+ " CR: " + str(ch1.getCR())+ " CS : " + str(ch1.getCS()) + " CE1 : " + str(ch1.getCE(1))
print "CH : " + ch2.getID() + " CC : " + str(ch2.getCC())+ " CR: " + str(ch2.getCR())+ " CS : " + str(ch2.getCS()) + " CE1 : " + str(ch2.getCE(1))
# test pour mettre toute la liste de Z dans un champ SQLITE (type BLOB) et le relire ensuite
li = repr([558.12, 556.57, 556.57, 558.12])
il = eval(li)
for i in range(len(il)):
	print il[i]

"""
