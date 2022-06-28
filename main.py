import math
from math import exp


x1 = float(input('Veuillez entrer le nombre de sujet neuronav ayant ressenti un effet (responders/remitters) x1: '))
x0 = float(input('Veuillez entrer le nombre de sujets control standard ayant ressenti un effet (responders/remitters) x0: '))
n1 = 45
n0 = 47


y1 = n1 - x1
y0 = n0 - x0

# calcul de RR
RR = float((x1 / n1) / (x0 / n0))
print('RR=', RR)

# calcul de l'IC 95% de RR

VarLogRR = float((1 / x1) - (1 / n1) + (1 / x0) - (1 / n0))


BinfRR = exp(math.log(RR) - 1.96 * math.sqrt(VarLogRR))
BsupRR = exp(math.log(RR) + 1.96 * math.sqrt(VarLogRR))

print('L IC 95% de RR est [', BinfRR, ';', BsupRR, ']')

# calcul de RD
RD = float((x1/n1)-(x0/n0))
print('RD=', RD)

#calcul de IC 95% de RD
SE = math.sqrt(((x1*y1)/(math.pow(n1,3))) + ((x0*y0)/(math.pow(n0,3))))

BinfRD = RD - 1.96*SE
BsupRD = RD + 1.96*SE

print('L IC 95% de RD est [', BinfRD, ';', BsupRD, ']')




